import argparse
import logging

from report.data.report_repo import ReportRepo
from report.domain.interactors.report_interactor import ReportInteractor


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def start_script(
    data: list[str], report_par: str, report_type: str
) -> None:
    logger.info('Запуск скрипта для получения отчета')
    report = ReportInteractor(report_repo=ReportRepo())
    report.create_report(data, report_par, report_type)
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
    args = parser.parse_args()
    start_script(
        args.data, args.report_par, args.report_type
    )
