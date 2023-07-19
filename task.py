from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.document = ""

    def handle_starttag(self, tag, attrs):
        if tag == 'button':
            for attr in attrs:
                if attr[0] == 'onclick':
                    eval(attr[1], globals(), locals())

    def handle_data(self, data):
        if data.strip():
            print(data.strip())

    def celsius_to_fahrenheit(self, celsius):
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius}°C is equal to {fahrenheit}°F")

    def fahrenheit_to_celsius(self, fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit}°F is equal to {celsius}°C")

def main():
    html_parser = MyHTMLParser()
    html_parser.document = '''
        <html>
            <div class='converter'>
                <h1>Temperature Converter</h1>
                <button onclick="html_parser.celsius_to_fahrenheit(float(document.getElementById('celsius').value))">Convert to Fahrenheit</button>
                <button onclick="html_parser.fahrenheit_to_celsius(float(document.getElementById('fahrenheit').value))">Convert to Celsius</button>
                <div id='slider'></div>
                <p id='sliderValue'>0°C</p>
            </div>
        </html>
    '''
    html_parser.feed(html_parser.document)

if __name__ == '__main__':
    main()

