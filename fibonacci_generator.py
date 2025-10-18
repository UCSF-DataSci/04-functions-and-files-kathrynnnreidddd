import argparse

def generate_fibonacci(limit):
    sequence = [0, 1]
    while sequence[-1] + sequence[-2] < limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def write_to_file(filename, data):
    try:
        with open(filename, "w") as f:
            f.write(", ".join(map(str, data)))
        print(f"Wrote {len(data)} Fibonacci numbers to {filename}")
    except IOError as e:
        print(f"File error: {e}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, required=True)
    parser.add_argument("--output", type=str, required=True)
    args = parser.parse_args()

    fibs = generate_fibonacci(args.limit)
    write_to_file(args.output, fibs)

if __name__ == "__main__":
    main()
