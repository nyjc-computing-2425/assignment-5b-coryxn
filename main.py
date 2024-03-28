# Part 1
def read_csv(filename):
  """
  takes in file name, returns its content in a tuple

  Parameter
  ---------
  filename: str
    name of file

  Returns
  -------
  tuple
    tuple in the format (header, data)
  """
  data = []
  with open(filename, 'r') as f:
    header = f.readline().strip().split(',')
    for line in f:
      rec = line.strip().split(',')
      rec[0] = int(rec[0])
      rec[3] = int(rec[3])
      data.append(rec)
    #f.close() is called automatically
    return data

# Part 2
def filter_gender(enrolment_by_age, sex):
  """
  takes in a list of records enrolment_by_age and a string sex, and return a list of records where the value in the "sex" column matches string sex, but excluding the "sex" columm

  Parameters
  ----------
  enrolment_by_age: list
    list of records
  sex: string
    gender of student

  Returns
  --------
  list
    a list of records where the value in the "sex" column matches string sex, but excluding the "sex" columm
  """
  filter = []
  for line in enrolment_by_age:
    if line[2] == sex:
      filter.append([line[0], line[1], line[3]])
  return filter

# Part 3
def sum_by_year(enrolment_data):
  """
  a list of total enrolment

  Parameters
  ----------
  enrolment: list
    list of data

  Returns
  -------
  list
    comprises two integers, year and total_enrolment
  """
  year_list = []
  sum_list = []
  sum = 0
  year_list.append(enrolment_data[1][0])
  for line in enrolment_data:
    year = line[0]
    if year != year_list[-1]:
      sum_list.append(sum)
      sum = 0
      year_list.append(year)
    else:
      sum += int(line[2])
  sum_list.append(sum)
  
  enrolment_by_year = []
  for i in range(len(year_list)):
    enrolment_by_year.append([year_list[i], sum_list[i]])
  return enrolment_by_year
  
# Part 4
def write_csv(filename, header, data):
  """
  write header and data to filename

  Parameters
  ------------
  filename: str
    name of file
  header: list
    header of file
  data: list
    list of data in file

  Returns
  --------
  tuple
    tuple in the format (header, data)
  """
  with open(filename, 'w') as f:
    output = ','.join(header)+'\n'
    f.write(output)
    count = 0
    for rec in data:
      output = f'{rec[0]}, {rec[1]}\n'
      f.write(output)
      count += 1
    #f.close() is called automatically
  return count


# TESTING
# You can write code below to call the above functions
# and test the output
  
enrolment_data = read_csv('pre-u-enrolment-by-age.csv')
# print(enrolment)

mf_enrolment = filter_gender(enrolment_data, "MF")
# print(mf_enrolment)

enrolment_by_year = sum_by_year(mf_enrolment)
# print(enrolment_by_year)

filename = 'total-enrolment-by-year.csv'
header = ["year", "total_enrolment"]
data = write_csv(filename, header, enrolment_by_year)
print(data)