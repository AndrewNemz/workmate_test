import logging
from pprint import pprint

from report.domain.repositories.report_repo import IReportRepo


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ReportInteractor:

    def __init__(self, report_repo: IReportRepo) -> None:
        self.report_repo = report_repo

    def create_report(
            self,
            data: list[str],
            report_par: str,
            report_type: str,
    ) -> None:
        logger.info(
            'Method create report start. '
            f'Тип отчета - {report_type}, '
            f'Параметр отчета - {report_par}'
        )
        try:
            match report_type:
                case 'json':
                    report = self.report_repo.create_json_report(
                        data=data, report_par=report_par
                    )
                case 'another type':
                    # self.report_repo.create_another_type_report()
                    pass
            pprint(report)
            return report
        except FileNotFoundError:
            logger.error('Файл данных не найден')
            raise FileNotFoundError
        except Exception as error:
            logger.error(f'Возникла ошибка - {error}')
