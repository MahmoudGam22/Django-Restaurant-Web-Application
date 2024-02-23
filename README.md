# Django-Restaurant-Web-Application
Django Restaurant Web Application is designed to provide a comprehensive solution for managing a restaurant's operations, including reservations, menu display, and order processing.

## Features
- User Authentication
- User Profile
- Reservation System
- Menu Display
- Order Placement
- Responsive Design

## Deployment on AWS
### Components
1. Amazon VPC (Virtual Private Cloud):
   - Creates an isolated network environment for application.
  
2. Public Subnets:
   - Two public subnets in different availability zones to host the web servers (EC2 instances).
   - Associated with a route table directing traffic to the Internet Gateway.
  
3. Private Subnets:
   - Two private subnets in different availability zones to host the PostgreSQL RDS instance.
   - Associated with a separate route table.
  
4. Internet Gateway:
   - Allows the web servers in the public subnets to access the internet.

5. Amazon EC2 (Elastic Compute Cloud):
   - Hosts the web servers running Django application.
   - Part of an Auto Scaling Group for automatic scaling based on demand.
   - Associated with a security group allowing inbound traffic on ports 80, 8000, and 22 (for SSH).
  
6. Auto Scaling Group:
   - Automatically adjusts the number of EC2 instances based on demand.
   - Configured with desired capacity, minimum and maximum instances, and scaling policies.
  
7. Load Balancer:
   - Distributes incoming traffic across multiple EC2 instances in the Auto Scaling Group.
   - Ensures high availability and improved fault tolerance.
  
8. Amazon RDS (Relational Database Service):
   - Hosts the PostgreSQL database for Django application.
   - Placed in the private subnets for added security.
   - Configured with a separate security group allowing inbound traffic on port 5432.
  
9. Security Groups:
   - EC2 Security Group: Allows inbound traffic on ports 80, 8000, and 22.
   - RDS Security Group: Allows inbound traffic on port 5432 from the EC2 instances and Load Balancer.
  
10. Route 53 (Optional):
    - Amazon Route 53 for domain registration and DNS management.

## Deployment Steps
1. VPC Setup:
   - Create a new VPC with an appropriate CIDR block.
   - Configure public and private subnets in different availability zones.
   - Create route tables for public and private subnets.
     
2. Internet Gateway and Route Setup:
   - Create an Internet Gateway and attach it to the VPC.
   - Update the route table for public subnets to direct internet-bound traffic through the Internet Gateway.
     
3. EC2 Instances (Web Servers) with Auto Scaling:
   - Launch an Auto Scaling Group of EC2 instances within public subnets.
   - Configure scaling policies based on demand.
   - Attach the instances to the Load Balancer.
     
4. Load Balancer Configuration:
   - Create a Load Balancer to distribute traffic among EC2 instances.
   - Configure health checks and listeners.
     
5. RDS Instance (PostgreSQL):
   - Launch an RDS instance in one of the private subnets.
   - Choose PostgreSQL as the database engine.
   - Configure the database settings, including username, password, and database name.
   - Attach a security group allowing traffic on port 5432.
     
6. Security Group Configuration:
   - Configure security groups for the EC2 instances, Load Balancer, and RDS instance to allow necessary inbound traffic.
   
7. DNS Configuration (Optional):
   - If using Route 53, configure the domain and update DNS records to point to the Load Balancer.
     
8. Application Deployment:
   - SSH into the EC2 instances or use deployment tools to clone and deploy your Django project.
   - Install required packages, migrate the database, and run the Django application.
     
9. Accessing the Application:
   - Access the web application through the public IP or domain associated with the Load Balancer.
     
This enhanced architecture provides scalability and high availability by automatically adjusting resources based on demand and distributing traffic across multiple instances using a Load Balancer. Adjustments can be made based on specific requirements and best practices.

## Deploy Your Project on EC2
- ` sudo yum -y update`
- `yum install git`
- `git clone "your repository link"`
- `cd My-Django-Project`
- `pip3 install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py runserver 0.0.0.0:8000 `

## AWS Architecture
![Highly Avaliable and Scalable AWS architecture](https://github.com/Mahmoudgaber114/Django-Restaurant-Web-Application/assets/65420063/151a2eed-8bb4-40bc-843c-9d7731c77bed)

