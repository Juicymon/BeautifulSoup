#import beautifulsoup and request here
import requests, json
from bs4 import BeautifulSoup


#function to get job list from url 'https://www.monster.com/jobs/search?q={role}&where={location}'
def getJobList(role,location):
    url = 'https://www.monster.com/jobs/search?q={role}&where={location}'
    # Complete the missing part of this function here

#save data in JSON file
def saveDataInJSON(jobDetails):
    #Complete the missing part of this function here
    print("Saving data to JSON")

#main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("Enter the location you want to search")
    location = input()

    ##url = getJobList(role, location)
    print(f'Role: {role}, Location: {location}')
    
if __name__ == '__main__':
    main()
