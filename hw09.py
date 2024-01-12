def total_time(fname, employee):
    '''
    Purpose:
        Find the total hours an employee worked according to their time sheet
    Parameters:
        fname - name of the file where hours were logged
        employee - name of employee we are looking to sum the hours of
    Return Value:
        The toal hours of the employee
    '''
    try:
        fp = open(fname)
        hours = 0.0
        list = []
        x = []
        for line in fp:
            y = line.strip()
            x = y.split(' ')
            if employee in line:
                list.append(float(x[1]))
        hours = sum(list)
        fp.close()
        return float(hours)
    except FileNotFoundError:
        return -1.0
    

if __name__ == '__main__':
    print(total_time('hours1', 'Leslie'))

def most_populous(year, region):
    '''
    Purpose:
        Find all of the most populous cities from the given year and given region
    Parameters:
        year - The year to look in
        region - The specific region to look in
    Return Value:
        Return a list of all the most populous cities  were from the given region in the given year.
    '''
    fp = open('cities.csv')
    fp.readline()
    list = []
    x = []
    for line in fp:
        row = line.strip()
        x = row.split(',')
        if x[0] == year and x[-1] == region:
            list.append(x[1])
    fp.close()
    return list

def stasis(jump_year, jump_city):
    '''
    Purpose: Increase the population of a city by 3000 for every year after the jump including it. 
    Parameters:
        jump_year - The year that the Witzidrema jumped to
        jump_city - The city the Witzidrema jumped to
    Return Value:
        The number of times the city population was updated
    '''
    fpin = open('cities.csv')
    fpout = open('fixed_'+'cities.csv', 'w')
    x = 0
    for line in fpin:
        row = line.split(',')
        if row[0] >= jump_year and row[1] == jump_city:
            row[3] = str(int(row[3]) + 3)
            x += 1
        new_line = ','.join(row)
        fpout.write(new_line)
    fpin.close
    fpout.close
    return x