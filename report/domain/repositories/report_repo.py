from abc import ABC, abstractmethod


class IReportRepo(ABC):

    @abstractmethod
    def create_json_report(
        self,
        data: list[str],
        report_par: str,
        report_name: str
    ) -> None:
        raise NotImplementedError

    @abstractmethod
    def _join_data(
        self,
        report_data,
        report_par
    ):
        raise NotImplementedError

    @abstractmethod
    def _get_file_data(
        self,
        file_data: str
    ):
        raise NotImplementedError

    @abstractmethod
    def _parse_line(self, line):
        raise NotImplementedError

    # @abstractmethod
    # def create_another_type_report(
    #     self,
    #     data: list[str],
    #     report_par: str,
    #     report_name: str
    # ) -> None:
    #     raise NotImplementedError
