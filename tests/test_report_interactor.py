import pytest

from report.data.report_repo import ReportRepo
from report.domain.interactors.report_interactor import ReportInteractor
from report.domain.repositories.report_repo import IReportRepo


class TestReportInteractor:
    @pytest.fixture
    def report_repo(self):
        return ReportRepo()

    @pytest.fixture
    def report_interactor(self, report_repo):
        return ReportInteractor(report_repo)

    def test_interactor_empty_data(
            self,
            report_interactor: ReportInteractor,
            report_repo: IReportRepo
    ):
        data = []
        report_par = 'payout'
        report_type = 'json'

        result = report_interactor.create_report(data, report_par, report_type)

        assert result is None

    def test_interactor_file_not_found(
            self,
            report_interactor: ReportInteractor,
            report_repo: ReportRepo
    ):
        data = ["non_existent_file.csv"]
        report_par = 'payout'
        report_type = 'json'

        with pytest.raises(FileNotFoundError):
            report_interactor.create_report(data, report_par, report_type)

    def test_create_report_another_type(
            self,
            report_interactor: ReportInteractor,
            report_repo: ReportRepo,
            tmpdir
    ):
        test_file = tmpdir.join("test.csv")
        content = "department,name,rate,hours_worked\ntest_dep,test_name,3,1"
        test_file.write_text(content, encoding='utf-8')
        data = [str(test_file)]
        report_par = 'test'
        report_type = 'another type'

        result = report_interactor.create_report(data, report_par, report_type)
        assert result is None

    def test_create_report_another_report_par(
            self,
            report_interactor: ReportInteractor,
            report_repo: ReportRepo,
            tmpdir
    ):
        test_file = tmpdir.join("test.csv")
        content = "department,name,rate,hours_worked\ntest_dep,test_name,3,1"
        test_file.write_text(content, encoding='utf-8')
        data = [str(test_file)]
        report_par = 'another report_par'
        report_type = 'json'

        result = report_interactor.create_report(data, report_par, report_type)
        assert result is None

    def test_create_report_success(
            self,
            report_interactor: ReportInteractor,
            report_repo: ReportRepo,
            tmpdir
    ):
        test_file = tmpdir.join("test.csv")
        content = "department,name,rate,hours_worked\ntest_dep,test_name,3,1"
        test_file.write_text(content, encoding='utf-8')
        data = [str(test_file)]
        report_par = 'payout'
        report_type = 'json'

        result = report_interactor.create_report(data, report_par, report_type)

        assert isinstance(result, dict)
        assert isinstance(result['test_dep'], dict)
        assert isinstance(result['test_dep']['test_name'], dict)
        assert result['test_dep']['test_name']['payout'] == 3.0
