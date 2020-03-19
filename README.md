# STA9760Project1
Analyzing Millions of NYC Parking Violations


Part 1
Read in data using API call


Part 2
Loading into ElacticSearch
output code
curl -o output.txt http://<docker's ip>:9200/bigdata1/_search?q=state:NY&size=10


Part 3

The first Kibana visualization shows that the county has the highest average reduction amount is Q.


![image](https://user-images.githubusercontent.com/57573785/77021057-1b0d8500-695c-11ea-8437-b766a7ec949d.png)


The second Kibana visualization shows that the most popular violation is PHTO SCHOOL ZN SPEED VIOLATION.
And the second most popular is NO PARKING-STREET CLEANING.

![image](https://user-images.githubusercontent.com/57573785/77021509-404ec300-695d-11ea-9415-5dc27e91b382.png)


The third Kibana visualization shows the highest average fine amount occurs for violations of "DOUBLE PARKING" and "BIKE LANE".



![image](https://user-images.githubusercontent.com/57573785/77023139-e69cc780-6961-11ea-9530-3219a011ea2c.png)


The fourth Kibana visualization shows the state with most license type is NY.


![image](https://user-images.githubusercontent.com/57573785/77024634-637d7080-6965-11ea-8881-bed43eb9b004.png)



