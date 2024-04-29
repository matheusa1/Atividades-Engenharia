class FileManager:
    def read_file(self, file_name):
        with open(file_name, 'r') as file:
            return file.read()

    def write_file(self, file_name, data):
        with open(file_name, 'w') as file:
            file.write(data)

class DataProcessor:
    def process_data(self, data):
        # Process data here
        return processed_data

    def save_processed_data(self, processed_data):
        file_manager = FileManager()
        file_manager.write_file('processed_data.txt', processed_data)

# Exemplo de uso
data = FileManager().read_file('data.txt')
processed_data = DataProcessor().process_data(data)
DataProcessor().save_processed_data(processed_data)


# Neste exemplo cada classe e cada método tem sua função, os métodos read_file e write_file, possuem uma função cada, e pertencem a classe
# FileManager, que também possui apenas uma função, gerir arquivos, o mesmo se repete para DataProcessor e seus métodos
