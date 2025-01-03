# Pet Adoption System

## Group Members:
- Varad Pawar
- Bhanu Prakash Putta

## Narrative
  
  The Pet Adoption System is designed to connect potential pet adopters with animals in need of a home. This application provides a platform where users can browse pets available for adoption, learn about each pet’s details, and submit adoption requests. Admins can manage pet listings, user information, and adoption requests. The system ensures a seamless adoption process by maintaining clear roles for different types of users and ensuring data integrity throughout the process.

### Primary Use Cases:

1. **View available pets for adoption** - Users can browse through pets listed by different shelters and view detailed information on each pet.
2. **Adopt a pet** - Potential adopters can submit an adoption request for a pet they are interested in.
3. **Manage pet listings** - Admins can add, update, or delete pet listings.
4. **View adoption requests** - Admins can review adoption requests and approve or deny them.
5. **User Registration and Login** - Users can create accounts, login, and manage their profiles.
6. **Book an Appointment** - A customer will have an option to book an appointment to adopt a pet from a shelter. By default it will have status 'Pending' and admin can update the appointment 'Scheduled', 'Completed', 'Cancelled'.

### User Roles:
1. **Admin**
   - Main Purpose: Admins have full control over the application. They can manage all user roles, review adoption requests, and make decisions about the adoption process.
   
2. **Customer**
   - Main Purpose: Adopters can view pet listings, submit adoption requests, and view shelter listing. They cannot manage user roles.

- **Note** - Fore future scope, we could implement a shelter owner role, where we could provide them much more functionality with adding pets, and making and updating appointments as needed.
   
### ER Diagram
![ER Diagram](./ER_Diagram.jpeg)


## Relationships

1. One shelter can have multiple customers
2. One shelter can have multiple pets available for adoption.
3. One user can make multiple appointments.⁠
4. One shelter can have multiple appointments.
5. One user can adopt multiple pets.
6. One pet can be adopted by only one user.

## Credentials per User Role

| User Role       | Username   | Password             |
|-----------------|------------|----------------------|
| Admin           | pawarv@example.com         | 134  |
| Customer        | bhanu@example.com          | 123  |
| Customer        | Tyler@example.com          | 1234 |


## SQL Queries

Here are some example queries from the project that we used to build the schema

```
  CREATE TABLE `VB_Adoptions` (
    `adoption_id` int NOT NULL,
    `request_date` datetime NOT NULL,
    `status` varchar(50) NOT NULL,
    `adoption_date` datetime DEFAULT NULL,
    `user_id` int DEFAULT NULL,
    `pet_id` int DEFAULT NULL
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------
-- SQL query for inserting data into table `VB_Adoptions`
-- --------------------------------------------------------

  INSERT INTO `VB_Adoptions` (`adoption_id`, `request_date`, `status`, `adoption_date`, `user_id`, `pet_id`) VALUES
  (1, '2024-11-01 00:00:00', 'Approved', '2024-11-15 00:00:00', 5, 3),
  (4, '2024-11-19 00:00:00', 'Pending', NULL, 8, 2),
  (5, '2024-11-19 00:00:00', 'Approved', '2024-11-19 00:00:00', 7, 1)

-- --------------------------------------------------------

--
-- SQL query for inserting data into table `VB_Appointments`
--

INSERT INTO `VB_Appointments` (`appointment_id`, `appointment_date`, `status`, `shelter_id`, `user_id`) VALUES
(3, '2024-11-19 00:00:00', 'Scheduled', 1, 8),
(4, '2024-12-01 14:02:35', 'Pending', 1, 5),
(7, '2024-12-10 13:19:13', 'Pending', 1, 5);


-- --------------------------------------------------------
-- Table structure for table `VB_Pets`
-- --------------------------------------------------------

CREATE TABLE `VB_Pets` (
  `pet_id` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `type` varchar(50) NOT NULL,
  `breed` varchar(50) NOT NULL,
  `age` int NOT NULL,
  `gender` varchar(50) NOT NULL,
  `health_status` varchar(50) NOT NULL,
  `description` varchar(50) NOT NULL,
  `image_url` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `listing_date` datetime NOT NULL,
  `status` varchar(50) NOT NULL,
  `shelter_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci; 

```


### Transactional vs Analytical Queries:

```
INSERT INTO `VB_Adoptions` (`adoption_id`, `request_date`, `status`, `adoption_date`, `user_id`, `pet_id`) VALUES
(1, '2024-11-01 00:00:00', 'Approved', '2024-11-15 00:00:00', 5, 3),
(4, '2024-11-19 00:00:00', 'Pending', NULL, 8, 2),
(5, '2024-11-19 00:00:00', 'Approved', '2024-11-19 00:00:00', 7, 1)

ALTER TABLE `VB_Users`
  ADD CONSTRAINT `VB_Users_ibfk_1` FOREIGN KEY (`shelter_id`) REFERENCES `VB_Shelters` (`shelter_id`);
COMMIT;




SELECT 
  CASE
    WHEN age < 1 THEN '0-1 years'
      WHEN age BETWEEN 1 AND 3 THEN '1-3 years'
      ELSE '3+ years'
      END as age_group,
  COUNT(*) as count
  FROM VB_Pets
  GROUP BY age_group;

SELECT gender, COUNT(*) as count
FROM VB_Pets
GROUP BY gender;
```

