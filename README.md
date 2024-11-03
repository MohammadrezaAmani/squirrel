# Squirrel: Iran Web Crawler

Squirrel is a web crawler that allows you to collect all pages from Iranian websites. Using this crawler, you can download the content of web pages and store it in a specified structure.

## Features

- Support for concurrent requests to optimize crawling speed
- Ability to set batch size for processing URLs
- Test mode to verify URLs without downloading content
- Content storage in a specified path

## Requirements

- Python 3.11 or higher
- Libraries: `aiohttp` and `aiofiles`

## Installation

To install this squirrel, simply use pip:

```bash
pip install aiohttp aiofiles
```

## Usage

To run the crawler, use the following command:

```bash
python -m squirrel [OPTIONS]
```

### Command-line Parameters

- `--max-concurrent`: Maximum number of concurrent requests (default: 50)
- `--batch-size`: Number of URLs processed in each batch (default: 10)
- `--skip-test`: Skip Running the crawler in test mode (default: disabled)
- `--base-path`: Storage path for downloaded content (default: `./data`)

### Example

To run the crawler with 20 concurrent requests and save data in the `my_data` directory, use the following command:

```bash
python -m squirrel --max-concurrent 20 --batch-size 5 --skip-test --base-path "./my_data"
```

## Contributing

If you would like to contribute to the development of this project, please create an issue or submit a pull request. All feedback and suggestions are welcome!

## License

This project is licensed under the MIT License. For more information, please refer to the LICENSE file.
