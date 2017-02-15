# Website Spider

version 1.0

## Basic Information

This spider is built for crawling news-link from websites.

This spider is customizble, you can change your spider setting in ```web/settings.py```.

This spider support multi-website crawling, you can set the rules separately.

You can also set the way to store the information you crawled. You change it in ```web/settings.py```.

## How to run my spider

You can use ```python main.py``` to run the menu

## How to setup my spider

You will find your spider settings in ```projectname/web/settings.py```

There are settings you can change:

### Basic Config

> URLS(array):
> > The website urls you want to crawl
> 
> PATH(dict):
> > items' xpath you want to crawl
> > 'ROOT': basic xpath of following information
> > 'TITLE'
> > 'LINK'

### Items Feed

> FEED_URI:
> > One way to store the informations, you store them in ```.json``` ```.jl``` ```.csv``` ```.xml```
> 
> FEED_FORMAT:
> > Choices: ```'json'``` ```'.jsonlines'``` ```'csv'``` ```'xml'``` ```'pickle'```
>

### Logging Config

> LOG_ENABLED
> 
> LOG_ENCODING
> 
> LOG_FILE
> 
> LOG_LEVEL
> 
> LOG_DATEFORMAT
> 
> LOG_STDOUT

### Cookies Config

> COOKIES_ENABLED
> 
> COOKIES

### Item Pipeline

> ITEM_PIPELINES

### Prevent Blocked

> AUTOTHROTTLE_ENABLED
> AUTOTHROTTLE_START_DELAY
> AUTOTHROTTLE_MAX_DELAY
> AUTOTHROTTLE_TARGET_CONCURRENCY
> AUTOTHROTTLE_DEBUG