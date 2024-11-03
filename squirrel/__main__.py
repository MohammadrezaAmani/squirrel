import argparse
import asyncio

from squirrel import main

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Web Crawler Configuration")
    parser.add_argument(
        "--max-concurrent",
        type=int,
        default=50,
        help="Maximum number of concurrent requests (default: 50)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=10,
        help="Number of URLs to process in each batch (default: 10)",
    )
    parser.add_argument(
        "--skip-test",
        action="store_true",
        help="Skip run in test mode (default: False)",
    )
    parser.add_argument(
        "--base-path",
        type=str,
        default="./data",
        help="Base path to save data (default: ./data)",
    )

    args = parser.parse_args()

    asyncio.run(
        main(
            max_concurrent=args.max_concurrent,
            batch_size=args.batch_size,
            skip_test=args.skip_test,
            base_path=args.base_path,
        )
    )
