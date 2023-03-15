# set it to use the virtualenv at the project root
#!
import argparse
import pdfminer as pm

from config import OUTPUT_PATH


def parse_args():
    parser = argparse.ArgumentParser(
        prog="contador de horas formativas UFPR",
        description="Script para computar suas HF baseado nos certificados salvos em um diretório",
        add_help=True,
        usage="python script.py -f <tabela base> -d <diretório> -o <arquivo de saída>",
    )

    parser.add_argument(
        "-f",
        "--file",
        help="tabela base de horas formativas",
        type=str,
        required=True,
    )

    parser.add_argument(
        "-d",
        "--dir",
        help="diretório onde estão os certificados",
        type=str,
        # required=True,
    )

    parser.add_argument(
        "-o",
        "--output",
        help="arquivo de saída",
        type=str,
        # required=True,
        default=OUTPUT_PATH,
    )

    return parser.parse_args()


def main():
    args = parse_args()
    output_path = args.output
    file_path = args.file
    dir_path = args.dir

    text = pm.extract_text(file_path)
    print(text)


if __name__ == "__main__":
    main()
