#import beautifulsoup and request here
import requests, json
from bs4 import BeautifulSoup


#function to get job list from url 
#f'https://www.talent.com/jobs?k={role}&l={location}'
def getJobList(role,location):
    url = f'https://www.talent.com/jobs?k={role}&l={location}'
    response = requests.get(url)
    print(response.status_code)

    soup = BeautifulSoup(response.text, 'html.parser')
    JobDetails = soup.find_all('div', class_='card card__job')
    jobArray = []
    for job in JobDetails:
        jobTitle = job.find('h2', class_='card__job-title').text.strip()
        company = job.find('div', class_='card__job-empname-label').text.strip()
        description = job.find('p', class_='card__job-snippet').text.replace('\n', '').replace("'","").strip()
        jobDetailsjson ={
            "Title": jobTitle,
            "Company": company,
            "Description": description   
            }
        jobArray.append(jobDetailsjson)
    # Complete the missing part of this function here
    return jobArray

#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON")
    with open("jobDetails.json", "w") as outfile:
        json.dump(jobDetails, outfile)

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("Enter the location you want to search")
    location = input()
    
    print(f'Role: {role}, Location: {location}')
    jobArray = getJobList(role, location)
    for job in jobArray:
        print(job)
    saveDataInJSON(jobArray)

    
if __name__ == '__main__':
    main()
