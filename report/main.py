import argparse
import logging


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def start_script(data: list, report_par: str, report_type: str, report_name: str) -> None:
    logger.info('Запуск скрипта для получения отчета')
    print(data, report_par, report_name, report_type)
    logger.info('Скрипт завершил работу')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Передаем аргументы в скрипт:'
    )
    parser.add_argument('data', nargs='+', type=str, help='CSV файлы данных')
    parser.add_argument(
        '--report',
        dest='report_par',
        type=str,
        required=True,
        help='Параметр, по которому формируется отчет отчета'
    )
    parser.add_argument(
        '--type',
        dest='report_type',
        type=str,
        default='json',
        help='Параметр, определяющий тип отчета, изначально - json'
    )
    parser.add_argument(
        '--report_name',
        dest='report_name',
        type=str,
        default='report',
        help='Название отчета'
    )
    args = parser.parse_args()
    start_script(args.data, args.report_par, args.report_type, args.report_name)
