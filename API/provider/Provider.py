import math
import requests as rq
from functools import reduce
from provider.AbstractDataProvider import AbstractDataProvider


class Provider(AbstractDataProvider):
    # DataProvider Implementations
    def fetch_repositories(self, parameters, sort, num_results):
        pages = self.pages_count(num_results)

        repositories = []
        queries = []
        for page_number, per_page in enumerate(pages):
            query_url = self.assemble_repository_query(parameters, sort, page_number + 1, per_page)
            queries.append(query_url)
            repositories.append(rq.get(query_url).json())

        return self.json_responses(repositories, queries)

    def fetch_readme_url(self, repo_full_name):
        base_url = 'https://api.github.com/repos'
        token = 'b5d003b1b520254348e27c74552f4367b7afb0cd'
        request_url = f'{base_url}/{repo_full_name}/readme?access_token={token}'

        try:
            response = rq.get(request_url)
        except rq.exceptions.RequestException as e:
            # TODO: Handle error
            print("ERROR HERE:")
            print(e, file=sys.stderr)

        response_json = response.json()
        readme_url = response_json['download_url']

        return readme_url

    # Auxiliar Methods
    def pages_count(self, num_results):
        page_count = []
        github_page_limit = 100

        for x in range(math.floor(num_results / github_page_limit)):
            page_count.append(github_page_limit)

        remainder = num_results % github_page_limit
        if remainder != 0:
            page_count.append(remainder)

        return page_count

    def assemble_repository_query(self, parameters, sort, page_number, per_page):
        base_url = "https://api.github.com/search/repositories?q="
        base_url += parameters + "+sort:" + sort + "&per_page=" + str(per_page) + "&page=" + str(page_number)
        return base_url

    def json_responses(self, responses, urls):
        json = {}
        json["repos"] = reduce(lambda accum, response: accum + response["items"], responses, [])
        json["urls"] = urls
        return json