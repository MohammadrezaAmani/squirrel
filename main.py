from asyncio import run

from squirrel import main

if __name__ == "__main__":
    run(
        main(
            max_concurrent=50,
            batch_size=5,
            skip_test=False,
            base_path="./data",
        )
    )
