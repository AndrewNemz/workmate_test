# workmate_test

python main.py data1.csv data2.csv ....  --report payout

# для просмотра покрытия тестами:
pytest tests/test_report_interactor.py --cov=report --cov-report term --cov-report html


# запуск тестов
cd tests/
pytest