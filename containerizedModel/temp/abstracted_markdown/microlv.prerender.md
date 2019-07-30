# Prerender Service @abstr_hyperlink 

Google, Facebook, Twitter, Yahoo, and Bing are constantly trying to view your website... but they don't execute javascript. That's why we built Prerender. Prerender is perfect for AngularJS SEO, BackboneJS SEO, EmberJS SEO, and any other javascript framework.

Behind the scenes, Prerender is a node server from @abstr_hyperlink that uses phantomjs to create static HTML out of a javascript page. We host this as a service at @abstr_hyperlink but we also open sourced it because we believe basic SEO is a right, not a privilege!

It should be used in conjunction with these middleware libraries to serve the prerendered HTML to crawlers for SEO. Get started in two lines of code using @abstr_hyperlink or @abstr_hyperlink .

Prerender adheres to google's `_escaped_fragment_` proposal, which we recommend you use. It's easy: \- Just add <meta name="fragment" content="!"> to the <head> of all of your pages \- If you use hash urls (#), change them to the hash-bang (#!) \- That's it! Perfect SEO on javascript pages.

Prerender includes lots of plugins, for example using Amazon S @abstr_number to cache your prerendered HTML.   
Prerender also starts multiple phantomjs processes to maximize throughput.

### 

## Middleware

This is a list of middleware available to use with the prerender service:

#### Official middleware

###### Javascript

  * @abstr_hyperlink (Express)



###### Ruby

  * @abstr_hyperlink (Rails)



###### Apache

  * @abstr_hyperlink 



###### Nginx

  * @abstr_hyperlink 



#### Community middleware

###### PHP

  * @abstr_hyperlink (Zend Framework @abstr_number )
  * @abstr_hyperlink (Symfony @abstr_number )
  * @abstr_hyperlink (Laravel)



###### Java

  * @abstr_hyperlink 



###### Grails

  * @abstr_hyperlink 



###### Nginx

  * @abstr_hyperlink 



###### Apache

  * @abstr_hyperlink 



Request more middleware for a different framework in this @abstr_hyperlink .

## How it works

This is a simple service that only takes a url and returns the rendered HTML (with all script tags removed).

Note: you should proxy the request through your server (using middleware) so that any relative links to CSS/images/etc still work.

`GET` http://service.prerender.io/https://www.google.com

`GET` http://service.prerender.io/https://www.google.com/search?q=angular

## Running locally

If you are trying to test Prerender with your website on localhost, you'll have to run the Prerender server locally so that Prerender can access your local dev website.

If you are running the prerender service locally. Make sure you set your middleware to point to your local Prerender server with:

`export PRERENDER_SERVICE_URL=<your local url>`
    
    
    $ npm install
    $ node server.js
    // also supports heroku style invocation using foreman
    $ foreman start
    

## Deploying your own on heroku
    
    
    $ git clone https://github.com/prerender/prerender.git
    $ cd prerender
    $ heroku create
    $ git push heroku master
    

# Customization

See @abstr_hyperlink to see how to customize the server.

You can clone this repo and run `server.js`   
OR   
use `npm install prerender --save` to create an express-like server with custom plugins

## Plugins

See @abstr_hyperlink to see how to create plugins.

We use a plugin system in the same way that Connect and Express use middleware. Our plugins are a little different and we don't want to confuse the prerender plugins with the prerender middleware, so we opted to call them "plugins".

Plugins are in the `lib/plugins` directory, and add functionality to the prerender service.

Each plugin can implement any of the plugin methods:

#### `init()`

#### `beforePhantomRequest(req, res, next)`

#### `onPhantomPageCreate(phantom, req, res, next)`

#### `afterPhantomRequest(req, res, next)`

#### `beforeSend(req, res, next)`

## Available plugins

### basicAuth

If you want to only allow access to your Prerender server from authorized parties, enable the basic auth plugin.

You will need to add the `BASIC_AUTH_USERNAME` and `BASIC_AUTH_PASSWORD` environment variables. @abstr_code_section 

Then make sure to pass the basic authentication headers (password base @abstr_number encoded).

@abstr_code_section 

### removeScriptTags

We remove script tags because we don't want any framework specific routing/rendering to happen on the rendered HTML once it's executed by the crawler. The crawlers may not execute javascript, but we'd rather be safe than have something get screwed up.

For example, if you rendered the HTML of an angular page but left the angular scripts in there, your browser would try to execute the angular routing and rendering on a page that no longer has any angular bindings.

### httpHeaders

If your Javascript routing has a catch-all for things like @abstr_number 's, you can tell the prerender service to serve a @abstr_number to google instead of a @abstr_number . This way, google won't index your @abstr_number 's.

Add these tags in the `<head>` of your page if you want to serve soft http headers. Note: Prerender will still send the HTML of the page. This just modifies the status code and headers being sent.

Example: telling prerender to server this page as a @abstr_number @abstr_code_section 

Example: telling prerender to serve this page as a @abstr_number redirect @abstr_code_section 

### whitelist

If you only want to allow requests to a certain domain, use this plugin to cause a @abstr_number for any other domains.

You can add the whitelisted domains to the plugin itself, or use the `ALLOWED_DOMAINS` environment variable.

`export ALLOWED_DOMAINS=www.prerender.io,prerender.io`

### blacklist

If you want to disallow requests to a certain domain, use this plugin to cause a @abstr_number for the domains.

You can add the blacklisted domains to the plugin itself, or use the `BLACKLISTED_DOMAINS` environment variable.

`export BLACKLISTED_DOMAINS=yahoo.com,www.google.com`

### 

### s @abstr_number HtmlCache

A `GET` request will check S @abstr_number for a cached copy. If a cached copy is found, it will return that. Otherwise, it will make the request to your server and then persist the HTML to the S @abstr_number cache.

A `POST` request will skip the S @abstr_number cache. It will make a request to your server and then persist the HTML to the S @abstr_number cache. The `POST` is meant to update the cache.

You'll need to sign up with Amazon Web Services and export these @abstr_number environment variables.

@abstr_code_section 

Warning! Your keys should be kept private and you'll be charged for all files uploaded to S @abstr_number .

> If Prerender is hosted on a EC @abstr_number instance, you can also take advantage of @abstr_hyperlink so that you don't need to export your AWS credentials.
> 
> You can also export the S @abstr_number _PREFIX_KEY variable so that the key (which is by default the complete requested URL) is prefixed. This is useful if you want to organize the snapshots in the same bucket.

#### Region support

By default, s @abstr_number HtmlCache works with the US Standard region (East), if your bucket is localized in another region you can config it with an environment variable : `AWS_REGION`.

@abstr_code_section 

For example :

@abstr_code_section 

### inMemoryHtmlCache

The default is an in memory cache but you can easily change it to any caching system compatible with the `cache-manager` nodejs package.

For example, with the request:

`GET` http://service.prerender.io/https://www.facebook.com/

First time: Overall Elapsed: @abstr_number : @abstr_number : @abstr_number . @abstr_number 

With cache: Overall Elapsed: @abstr_number : @abstr_number : @abstr_number . @abstr_number 

### logger

This will show console.log's from the phantomjs page in your local console. Great for debugging.

### mongodbCache

Caches pages in a MongoDB database. Available at @abstr_hyperlink by @abstr_hyperlink 

### memjsCache

Caches pages in a memjs(memcache) service. Available at @abstr_hyperlink by @abstr_hyperlink 

## License

The MIT License (MIT)

Copyright (c) @abstr_number Todd Hooper <todd@prerender.io>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.