import csv
import os

class CSVReader:
    @staticmethod
    def read_csv(filename):
        """
        Read CSV file and return list of dictionaries
        """
        filepath = os.path.join(
            os.path.dirname(__file__),
            '..',
            'test_data',
            filename
        )
        
        data = []
        with open(filepath, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        
        return data
    
    @staticmethod
    def get_login_data():
        """
        Get login test data
        Returns list of tuples (username, password, expected)
        """
        data = CSVReader.read_csv('users.csv')
        return [
            (row['username'], row['password'], row['expected_result'])
            for row in data
        ]