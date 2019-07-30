## Introduction

[git-tfs](http://git-tfs.com/) is a two-way bridge between TFS (Team Foundation Server) and git, similar to git-svn.
It fetches TFS commits into a git repository, and lets you push your updates back to TFS.

[![git-tfs version](https://img.shields.io/github/release/git-tfs/git-tfs.svg?label=Actual%20Version:)](https://github.com/git-tfs/git-tfs/releases). See the [change history](https://github.com/git-tfs/git-tfs/releases) for details and download.

If you're having problems, check out the [troubleshooting](doc/TROUBLESHOOTING.md) page.
And read [how to report an issue](doc/reporting-issues.md), before doing so ;)

## We need your help

This project is no more **actively** maintained because we are no more users of TFS.
Thus being very useful, git-tfs is not exempt of not supported use cases.
If you encounter something missing or a problem, please contribute, we will be pleased to help you.

And remember:

>The fastest way to get an issue fixed is to submit a PR that fixes it.

>The slowest way to get it fixed is to hope someone else will fix it.

## Get git-tfs

To get a stable version:

* Download a binary. Find it on the [release page](https://github.com/git-tfs/git-tfs/releases),
* Using Chocolatey. If [Chocolatey](http://chocolatey.org/) is already installed on your computer, run `choco install gittfs` to install the [Chocolatey package](http://chocolatey.org/packages/gittfs)

To get a development version

* Build from source code. See §[Building](#building) for more informations...
* Download a package of the development version generated by the [last builds](https://ci.appveyor.com/project/pmiossec/git-tfs-v2qcm/build/artifacts) (in the artifacts section).

__Whatever the way you get git-tfs, you should have git-tfs.exe in your path (and git, too)__.

Add the git-tfs folder path to your PATH. You could also set it temporary (the time of your current terminal session) using :

    set PATH=%PATH%;%cd%\GitTfs\bin\Debug

## Use git-tfs

You need .NET 4.5.2 and maybe the 2012 or 2013 version of Team Explorer installed (or Visual Studio) depending on the version of TFS you want to target.

### Help

    #lists the available commands
    git tfs help

    #shows a summary of the usage of a given command
    git tfs help <command>

### Cloning

    # [optional] find a tfs repository path to clone :
    git tfs list-remote-branches http://tfs:8080/tfs/DefaultCollection

    # clone the whole repository (wait for a while...) :
    git tfs clone http://tfs:8080/tfs/DefaultCollection $/some_project

    # or, if you're impatient (and want to work from the last changeset) :
    git tfs quick-clone http://tfs:8080/tfs/DefaultCollection $/some_project

    # or, if you're impatient (and want a specific changeset) :
    git tfs quick-clone http://tfs:8080/tfs/DefaultCollection $/some_project -c=145

**Note:** Before cloning your repository, please have a look at the [clone command doc](doc/commands/clone.md) or [advanced use cases](#more-advanced-use-cases) to discover options that could help you!

### Working

    cd some_project
    git log # shows your TFS history, unless you did quick-clone
    tf history # error: no workspace ;)

    # [do work, do work, just using git], then...
    # gets latest from TFS to the branch tfs/default :
    git tfs fetch

### Checkin

    # report all the commits on TFS :
    git tfs rcheckin

    # or commit using the tfs checkin window
    git tfs checkintool

    # or commit with a message
    git tfs checkin -m "Did stuff"

    # or shelve your changes :
    git tfs shelve MY_AWESOME_CHANGES

git-tfs is designed to work outside of any existing TFS workspaces.

### More advanced use cases

Have a look to more detailed git-tfs use cases:

* [Working with no branches](doc/usecases/working_with_no_branches.md)
* [Manage TFS branches with git-tfs](doc/usecases/manage_tfs_branches.md)
* [Migrate your history from TFSVC to a git repository](doc/usecases/migrate_tfs_to_git.md)
* [Working with shelvesets](doc/usecases/working_with_shelvesets.md)
* [Git and Tfs (ProGit v2 Book)](https://git-scm.com/book/en/v2/Git-and-Other-Systems-Git-as-a-Client#_git_and_tfs)
* [Migrate from Tfs to Git (ProGit v2 Book)](https://git-scm.com/book/en/v2/Git-and-Other-Systems-Migrating-to-Git#_git_tfs)

## Available commands / options

This is the complete list of commands in the master branch on github.

### Repository setup

* [list-remote-branches](doc/commands/list-remote-branches.md): *list tfs branches that can be cloned or initialized* - since [0.17](../../releases/tag/v0.17.0)
* [clone](doc/commands/clone.md): *clone a tfs path/branch and its history in a git repository* - since 0.9
* [quick-clone](doc/commands/quick-clone.md): *clone a specific changeset of a tfs path/branch in a git repository* - since 0.9
* [bootstrap](doc/commands/bootstrap.md): *bootstrap an existing git-tfs repository cloned from an existing repository* - since [0.11][v0.11]
* [init](doc/commands/init.md): *initialize a git-tfs repository (without getting changesets)* - since 0.9

### Pull from TFS

* [clone](doc/commands/clone.md): *clone a tfs path/branch and its history in a git repository* - since 0.9
* [fetch](doc/commands/fetch.md): *get changesets from tfs and update the tfs remote* - since 0.9
* [pull](doc/commands/pull.md): *get changesets from tfs, update the tfs remote and update your work* - since 0.9
* [quick-clone](doc/commands/quick-clone.md): *clone a specific changeset (without history) of a tfs path/branch in a git repository* - since 0.9
* [unshelve](doc/commands/unshelve.md): *fetch a tfs shelvesets in your repository* - since [0.11][v0.12]
* [shelve-list](doc/commands/shelve-list.md): *list tfs shelvesets* - since [0.12][v0.12]
* [labels](doc/commands/labels.md): *fetch tfs labels* - since [0.17](../../releases/tag/v0.17.0)

### Push to TFS

⚠ Read absolutely [this](doc/using-checkin-policies.md) if your TFVC repository use **Checkin policies** when check-in.

* [rcheckin](doc/commands/rcheckin.md): *replicate your git commits as tfs changesets* - since [0.12][v0.12]
* [checkin](doc/commands/checkin.md): *checkin your git commits as one tfs changeset* - since 0.10
* [checkintool](doc/commands/checkintool.md): *checkin in tfs using the tfs checkin dialog* - since 0.10
* [shelve](doc/commands/shelve.md): *create a shelveset from git commits* - since 0.9
* [shelve-delete](doc/commands/shelve-delete.md): *delete a shelveset on tfs* - since 0.25

### Manage TFS branches

* [list-remote-branches](doc/commands/list-remote-branches.md): *list tfs branches that can be cloned or initialized* - since [0.17](../../releases/tag/v0.17.0)
* [branch](doc/commands/branch.md): *manage (initialize, create, remove) tfs branches* - since [0.17](../../releases/tag/v0.17.0)

### Other

* [info](doc/commands/info.md): *get some informations about git-tfs and tfs*
* [cleanup](doc/commands/cleanup.md): *clean some git-tfs internal objects* - since 0.10
* [cleanup-workspaces](doc/commands/cleanup-workspaces.md): *clean tfs workspaces created by git-tfs* - since 0.10
* [help](doc/commands/help.md): *get help on git-tfs commands* - since 0.9
* [verify](doc/commands/verify.md): *verify the changesets fetched* - since [0.11][v0.11]
* [autotag](doc/config.md#per-tfs-remote) option - since [0.12][v0.12]
* [subtree](doc/commands/subtree.md): *manage sparse tfs pathes with git-tfs* - since [0.19](../../releases/tag/v0.19.0)
* [reset-remote](doc/commands/reset-remote.md): *reset a tfs remote to a previous changeset to fetch again its history* - since [0.19](../../releases/tag/v0.19.0)
* [checkout](doc/commands/checkout.md): *checkout a commit by a changeset id* - since [0.21](../../releases/tag/v0.21.0)
* diagnostics (for git-tfs developers only) - since 0.9

* [config file](doc/config.md)

## Building

### Continuous Integration Status

[![AppVeyor build status](https://ci.appveyor.com/api/projects/status/github/git-tfs/git-tfs?branch=master&svg=true&passingText=build%20%27master%27%20OK)](https://ci.appveyor.com/project/pmiossec/git-tfs-v2qcm)
( Great thanks to [<img src="https://www.appveyor.com/assets/img/favicons/favicon.ico" height="20"> AppVeyor](http://www.appveyor.com/)! )

### Prerequisites

* MSBuild (included in .NET 4)
* Visual Studio >= 2012 (preferably >= 2015)

### Get the source code and build

    #get the source code
    git clone git://github.com/git-tfs/git-tfs.git
    cd git-tfs\src

    #building with Cake (in a powershell console). It will also run the unit tests ;)
    .\build.ps1

    #help on the different targets
    .\build.ps1 -Target "Help"

**Note:** if the build fails to build some `GitTfs.Vs201x` projects, just unload in Visual Studio all the projects you are not interested in to be able to build and use your own version.
You could also install, the Team Foundation Server Object Model for [Tfs 2012](https://visualstudiogallery.msdn.microsoft.com/f30e5cc7-036e-449c-a541-d522299445aa) ([chocolatey](https://chocolatey.org/packages/tfs2012objectmodel)) and [Tfs 2013](https://visualstudiogallery.msdn.microsoft.com/3278bfa7-64a7-4a75-b0da-ec4ccb8d21b6) ([chocolatey](https://chocolatey.org/packages/tfs2013objectmodel)).

## Contributing
Contributions are always welcome. Thanks to all our [contributors](https://github.com/git-tfs/git-tfs/graphs/contributors)!

Please, read our short and simple [guidelines](CONTRIBUTING.md) and our doc on how to use [paket](doc/paket.md), the package manager we use.

Especially, don't forget:

* to run the build task `.\build.ps1 -Target "FormatCode"` before committing (to keep code formatting consistent, and pull request easier to review)
* to set `core.autocrlf` to `true` (`git config core.autocrlf true`)
* to indent your code using 4 spaces (even if `.editorconfig` should take care of that).

## Migrations
If you're migrating a TFS server from 2008 or 2005 to 2010, you might want to [Specify Alternate TFS URLs](doc/specify-alternate-tfs-urls.md).

[v0.11]: http://mattonrails.wordpress.com/2011/03/11/git-tfs-0-11-0-release-notes/ "0.11 Release notes"
[v0.12]: http://sparethought.wordpress.com/2011/08/10/git-tfs-bridge-v0-12-released/

If you have questions or suggestions about how we could improve git-tfs you could go to [google group](http://groups.google.com/group/git-tfs-dev).

[Example](http://sparethought.wordpress.com/2011/07/18/how-to-establish-git-central-repository-for-working-against-tfs-with-git-tfs-bridge/) of setting up central git repository that tracks TFS automatically.

## Community

Drop in and chat in [![gitter](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/git-tfs/git-tfs?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
We also have a [mailing list](https://groups.google.com/group/git-tfs-dev).