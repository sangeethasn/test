date = raw_input('Enter the date:')
new_date = date.split('-')
month = {
    '01': 'January',
    '02': 'Feb',
    '03': 'March',
    '04': 'April',
    '05': 'May',
    '06': 'June',
    '07': 'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
}
for i in month:
          print new_date[0],month[new_date[1]] , '20' +str(new_date[2])
          break


