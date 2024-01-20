import requests
from bs4 import BeautifulSoup



def get_constructors_championship(year):
    url = f'https://www.formula1.com/en/results.html/{year}/team.html'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')

    formatted_data = []
    if table:
        for row in table.find_all('tr')[1:]:
            data = [cell.get_text(strip=True) for cell in row.find_all('td')]
            formatted_data.append({
                'position': data[1],
                'team': data[2], 
                'points': int(data[3])
                })
        return formatted_data
    else:
        return f"no data available for the year {year}"
    
def get_constructor_at_position(year, position):
    url = f'https://www.formula1.com/en/results.html/{year}/team.html'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')

    if table:
        try:
            row = table.find_all('tr')[position]  
            data = [cell.get_text(strip=True) for cell in row.find_all('td')]
            return {
                'team': data[2],
                'points': int(data[3])
            }
        except IndexError:
            return f"no driver data available for position {position} in the year {year}"
    else:
        return f"no data available for the year {year}"
    
def get_drivers_championship(year):
    url = f'https://www.formula1.com/en/results.html/{year}/drivers.html'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')

    formatted_data = []
    if table:
        for row in table.find_all('tr')[1:]:  
            name_parts = row.find_all('span', class_=lambda x: x in ["hide-for-tablet", "hide-for-mobile"])
            full_name = ' '.join(part.get_text(strip=True) for part in name_parts if part.get_text(strip=True))
            points = row.find_all('td')[5].get_text(strip=True)
            position = row.find_all('td')[1].get_text(strip=True)
            formatted_data.append({
                'position': position,
                'driver': full_name, 
                'points': int(points)
                })
        return formatted_data
    else:
        return f"no data available for the year {year}"
    
def get_drivers_championship_code(year):
    url = f'https://www.formula1.com/en/results.html/{year}/drivers.html'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')

    formatted_data = []
    if table:
        for row in table.find_all('tr')[1:]:  
            name_parts = row.find_all('span', class_=lambda x: x and "hide-for-desktop" in x)
            full_name = ' '.join(part.get_text(strip=True) for part in name_parts if part.get_text(strip=True))
            points = row.find_all('td')[5].get_text(strip=True)
            position = row.find_all('td')[1].get_text(strip=True)
            formatted_data.append({
                'position': position,
                'driver': full_name, 
                'points': int(points)
                })
        return formatted_data
    else:
        return f"no data available for the year {year}"

def get_driver_at_position(year, position):
    url = f'https://www.formula1.com/en/results.html/{year}/drivers.html'
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    table = soup.find('table', class_='resultsarchive-table')

    if table:
        try:
            row = table.find_all('tr')[position]  
            name_parts = row.find_all('span', class_=lambda x: x in ["hide-for-tablet", "hide-for-mobile"])
            full_name = ' '.join(part.get_text(strip=True) for part in name_parts)
            points = row.find_all('td')[5].get_text(strip=True)  
            return {
                'driver': full_name,
                'points': int(points)
            }
        except IndexError:
            return f"no driver data available for position {position} in the year {year}"
    else:
        return f"no data available for the year {year}"


while True:
    user_input = input("?")
    if user_input.lower() == 'q':
        break

    parts = user_input.split()
    if len(parts) == 2 and parts[0].lower() == 'c':
        try:
            year = int(parts[1])
            constructors_list = get_constructors_championship(year)
            for row in constructors_list:
                print(f"{row['position']}.{row['team']}: {row['points']}")
        except ValueError:
            print("enter valid year")
    elif len(parts) == 2 and parts[0].lower() == 'd':
        try:
            year = int(parts[1])
            drivers_list = get_drivers_championship(year)
            for row in drivers_list:
                print(f"{row['position']}.{row['driver']}: {row['points']}")
        except ValueError:
            print("enter valid year")
    elif len(parts) == 3 and parts[0].lower() == 'd' and parts[2].lower() == 'u':
        try:
            year = int(parts[1])
            drivers_list = get_drivers_championship_code(year)
            for row in drivers_list:
                print(f"{row['position']}.{row['driver']}: {row['points']}")
        except ValueError:
            print("enter valid year")
    elif len(parts) == 4 and parts[0].lower() == 's' and parts[1].lower() == 'd':
        try:
            year = int(parts[2])
            pos = int(parts[3])
            driver = get_driver_at_position(year, pos)
            print(f"{driver['driver']}")
        except ValueError:
            print("enter valid year")
    elif len(parts) == 4 and parts[0].lower() == 's' and parts[1].lower() == 'c':
        try:
            year = int(parts[2])
            pos = int(parts[3])
            constructor = get_constructor_at_position(year, pos)
            print(f"{constructor['team']}")
        except ValueError:
            print("enter valid year")
