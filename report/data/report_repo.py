import logging
import os

from report.domain.repositories.report_repo import IReportRepo


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ReportRepo(IReportRepo):
    def create_json_report(self, data: list[str], report_par: str) -> dict:
        logger.info('Method create_json_report start')
        try:
            report_data = {}
            match report_par:
                case 'payout':
                    for file in data:
                        filename = os.path.basename(file)
                        file_data = self._get_file_data(file)
                        if file_data:
                            report_data[filename] = file_data
                        report = self._join_data(report_data, report_par)
                case 'another report_par':
                    # Добавьте здесь отчет нового типа
                    pass
            return report
        except FileNotFoundError:
            raise FileNotFoundError
        except Exception as error:
            raise error

    def _join_data(self, report_data, report_par):
        logger.info('Method join_data start')
        try:
            transformed_data = {}

            for filename, employees in report_data.items():
                for employee in employees:
                    department = employee['department']
                    name = employee.get('name')
                    rate = employee.get('rate') or employee.get('hourly_rate') or employee.get('salary')
                    hours_worked = employee.get('hours_worked')

                    if department not in transformed_data:
                        transformed_data[department] = {}
                    transformed_data[department][name] = {
                        'rate': rate,
                        'hours_worked': hours_worked,
                        'payout': float(rate)*float(hours_worked)
                        }

            return transformed_data
        except Exception as error:
            raise error

    def _get_file_data(self, file_data: str):
        logger.info(f'Method get_file_data start work with {file_data}')
        try:
            data = []
            with open(file_data, 'r', encoding='utf-8') as file:
                headers = self._parse_line(file.readline())

                for line in file:
                    values = self._parse_line(line)
                    recorded_data = {
                        header: value for header, value in zip(headers, values)
                    }
                    data.append(recorded_data)
        except FileNotFoundError:
            raise FileNotFoundError
        except Exception as error:
            logger.error(f'Ошибка при чтении {file_data}: {error}')

        return data

    def _parse_line(self, line):
        logger.info(f'Method parse_line start working with {line}')
        try:
            in_quotes = False
            fields = []
            current_field = []

            for char in line.strip():
                if char == '"':
                    in_quotes = not in_quotes
                elif char == ',' and not in_quotes:
                    fields.append(''.join(current_field))
                    current_field = []
                else:
                    current_field.append(char)

            if current_field:
                fields.append(''.join(current_field))

            return fields
        except Exception as error:
            logger.error(f'Ошибка при работе со строкой {line}: {error}')
