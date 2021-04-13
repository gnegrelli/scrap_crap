# scrap_crap

Project to scrape some data from a list of websites.

## Installation

Create a virtual environment and activate it via:

```bash
$ python3 -m venv venv
$ . venv/bin/activate
```

Install required packages via:

```bash
(venv)$ pip install -r requirements.txt
```

## Usage

You can run crawlers via command line with the following:

```bash
(venv)$ scrapy crawl my_spider -a filename=path/to/urls.txt
```

The targeted urls must be provided by the `path/to/urls.txt` argument above.
