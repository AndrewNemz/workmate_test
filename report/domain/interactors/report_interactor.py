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

        match report_type:
            case 'json':
                json_report = self.report_repo.create_json_report(
                    data=data, report_par=report_par
                )
                pprint(json_report)
            case 'another type':
                # self.report_repo.create_another_type_report()
                pass
