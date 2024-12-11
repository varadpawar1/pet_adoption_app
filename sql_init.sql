-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: db:3306
-- Generation Time: Dec 11, 2024 at 07:42 PM
-- Server version: 8.0.34
-- PHP Version: 8.2.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `ia637`
--

-- --------------------------------------------------------

--
-- Table structure for table `VB_Adoptions`
--

CREATE TABLE `VB_Adoptions` (
  `adoption_id` int NOT NULL,
  `request_date` datetime NOT NULL,
  `status` varchar(50) NOT NULL,
  `adoption_date` datetime DEFAULT NULL,
  `user_id` int DEFAULT NULL,
  `pet_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `VB_Adoptions`
--

INSERT INTO `VB_Adoptions` (`adoption_id`, `request_date`, `status`, `adoption_date`, `user_id`, `pet_id`) VALUES
(1, '2024-11-01 00:00:00', 'Approved', '2024-11-15 00:00:00', 5, 3),
(4, '2024-11-19 00:00:00', 'Pending', NULL, 8, 2),
(5, '2024-11-19 00:00:00', 'Approved', '2024-11-19 00:00:00', 7, 1),
(7, '2024-11-15 00:00:00', 'Pending', NULL, 8, 3),
(8, '2024-12-01 14:03:11', 'Pending', NULL, 5, 3),
(9, '2024-12-08 19:17:46', 'Pending', NULL, 5, 2);

-- --------------------------------------------------------

--
-- Table structure for table `VB_Appointments`
--

CREATE TABLE `VB_Appointments` (
  `appointment_id` int NOT NULL,
  `appointment_date` datetime NOT NULL,
  `status` varchar(50) NOT NULL,
  `shelter_id` int NOT NULL,
  `user_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `VB_Appointments`
--

INSERT INTO `VB_Appointments` (`appointment_id`, `appointment_date`, `status`, `shelter_id`, `user_id`) VALUES
(3, '2024-11-19 00:00:00', 'Scheduled', 1, 8),
(4, '2024-12-01 14:02:35', 'Scheduled', 1, 5),
(7, '2024-12-10 13:19:13', 'Scheduled', 1, 5);

-- --------------------------------------------------------

--
-- Table structure for table `VB_Pets`
--

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

--
-- Dumping data for table `VB_Pets`
--

INSERT INTO `VB_Pets` (`pet_id`, `name`, `type`, `breed`, `age`, `gender`, `health_status`, `description`, `image_url`, `listing_date`, `status`, `shelter_id`) VALUES
(1, 'Buddy', 'Dog', 'Golden Retriever', 3, 'Male', 'Healthy', 'A friendly and active dog looking for a home.', 'Buddy.png', '2024-11-18 00:00:00', 'Available', 1),
(2, 'Tom', 'Dog', 'Husky', 2, 'Male', 'Good', 'Good', 'https://potsdamhumanesociety.org/wp-content/upload', '2024-11-19 00:00:00', 'Available', 2),
(3, 'Blacky', 'Cat', 'Ragdoll', 1, 'Female', 'Very Healthy', 'Perfect match', 'https://potsdamhumanesociety.org/wp-content/upload', '2024-11-11 00:00:00', 'Available', 1),
(4, 'Buddy', 'Dog', 'Labrador Retriever', 3, 'Male', 'Healthy', 'Friendly and energetic', 'Buddy.png', '2024-01-01 00:00:00', 'Available', 1),
(5, 'Mittens', 'Cat', 'Siamese', 2, 'Female', 'Healthy', 'Loves cuddles', 'Mittens.png', '2024-01-02 00:00:00', 'Available', 1),
(6, 'Max', 'Dog', 'Golden Retriever', 5, 'Male', 'Healthy', 'Gentle and loyal', 'Max.png', '2024-01-03 00:00:00', 'Available', 1),
(7, 'Luna', 'Cat', 'Persian', 1, 'Female', 'Healthy', 'Playful and curious', 'Luna.png', '2024-01-04 00:00:00', 'Available', 1),
(8, 'Rocky', 'Dog', 'Bulldog', 4, 'Male', 'Healthy', 'Loves short walks', 'Rocky.png', '2024-01-05 00:00:00', 'Available', 1),
(9, 'Bella', 'Dog', 'Beagle', 2, 'Female', 'Healthy', 'Friendly and curious', 'Bella.png', '2024-01-06 00:00:00', 'Available', 2),
(10, 'Shadow', 'Cat', 'Maine Coon', 3, 'Male', 'Healthy', 'Independent and calm', 'Shadow.png', '2024-01-07 00:00:00', 'Available', 2),
(11, 'Charlie', 'Dog', 'Poodle', 6, 'Male', 'Healthy', 'Highly intelligent', 'Charlie.png', '2024-01-08 00:00:00', 'Available', 2),
(12, 'Cleo', 'Cat', 'Russian Blue', 1, 'Female', 'Healthy', 'Shy but affectionate', 'Cleo.png', '2024-01-09 00:00:00', 'Available', 2),
(13, 'Rex', 'Dog', 'German Shepherd', 4, 'Male', 'Healthy', 'Protective and obedient', 'Rex.png', '2024-01-10 00:00:00', 'Available', 2),
(14, 'Daisy', 'Dog', 'Shih Tzu', 2, 'Female', 'Healthy', 'Friendly and quiet', 'Daisy.png', '2024-01-11 00:00:00', 'Available', 3),
(15, 'Whiskers', 'Cat', 'Bengal', 3, 'Male', 'Healthy', 'Energetic and playful', 'Whiskers.png', '2024-01-12 00:00:00', 'Available', 3),
(16, 'Molly', 'Dog', 'Border Collie', 5, 'Female', 'Healthy', 'Highly active and smart', 'Molly.png', '2024-01-13 00:00:00', 'Available', 3),
(17, 'Tiger', 'Cat', 'Tabby', 2, 'Male', 'Healthy', 'Adventurous and loving', 'Tiger.png', '2024-01-14 00:00:00', 'Available', 3),
(18, 'Bailey', 'Dog', 'Corgi', 4, 'Female', 'Healthy', 'Loves running around', 'Bailey.png', '2024-01-15 00:00:00', 'Available', 3),
(19, 'Simba', 'Cat', 'Savannah', 3, 'Male', 'Healthy', 'Curious and active', 'Simba.png', '2024-01-16 00:00:00', 'Available', 4),
(20, 'Oscar', 'Dog', 'Dachshund', 2, 'Male', 'Healthy', 'Loves to dig and explore', 'Oscar.png', '2024-01-17 00:00:00', 'Available', 4),
(21, 'Lucy', 'Dog', 'Chihuahua', 1, 'Female', 'Healthy', 'Tiny but brave', 'Lucy.png', '2024-01-18 00:00:00', 'Available', 4),
(22, 'Duke', 'Dog', 'Great Dane', 3, 'Male', 'Healthy', 'Gentle giant', 'Duke.png', '2024-01-19 00:00:00', 'Available', 4),
(23, 'Snowball', 'Cat', 'Ragdoll', 2, 'Female', 'Healthy', 'Affectionate and relaxed', 'Snowball.png', '2024-01-20 00:00:00', 'Available', 4),
(24, 'Leo', 'Cat', 'Abyssinian', 1, 'Male', 'Healthy', 'Playful and agile', 'Leo.png', '2024-01-21 00:00:00', 'Available', 5),
(25, 'Toby', 'Dog', 'Boxer', 4, 'Male', 'Healthy', 'Energetic and strong', 'Toby.png', '2024-01-22 00:00:00', 'Available', 5),
(26, 'Sasha', 'Dog', 'Husky', 3, 'Female', 'Healthy', 'Loves cold weather', 'Sasha.png', '2024-01-23 00:00:00', 'Available', 5),
(27, 'Nala', 'Cat', 'Sphynx', 1, 'Female', 'Healthy', 'Unique and friendly', 'Nala.png', '2024-01-24 00:00:00', 'Available', 5),
(28, 'Chester', 'Dog', 'Dalmation', 5, 'Male', 'Healthy', 'Loves to run', 'Chester.png', '2024-01-25 00:00:00', 'Available', 5),
(29, 'Lily', 'Cat', 'Birman', 2, 'Female', 'Healthy', 'Gentle and affectionate', 'Lily.png', '2024-01-26 00:00:00', 'Available', 6),
(30, 'Zeus', 'Dog', 'Rottweiler', 4, 'Male', 'Healthy', 'Strong and loyal', 'Zeus.png', '2024-01-27 00:00:00', 'Available', 6),
(31, 'Ginger', 'Cat', 'Calico', 3, 'Female', 'Healthy', 'Colorful and loving', 'Ginger.png', '2024-01-28 00:00:00', 'Available', 6),
(32, 'Finn', 'Dog', 'Cocker Spaniel', 2, 'Male', 'Healthy', 'Cheerful and friendly', 'Finn.png', '2024-01-29 00:00:00', 'Available', 6),
(33, 'Pepper', 'Cat', 'Bombay', 1, 'Female', 'Healthy', 'Playful and sleek', 'Pepper.png', '2024-01-30 00:00:00', 'Available', 6),
(34, 'Duke', 'Dog', 'Doberman', 5, 'Male', 'Healthy', 'Protective and intelligent', 'Duke.png', '2024-01-31 00:00:00', 'Available', 7),
(35, 'Coco', 'Cat', 'Himalayan', 3, 'Female', 'Healthy', 'Sweet and calm', 'Coco.png', '2024-02-01 00:00:00', 'Available', 7),
(36, 'Marley', 'Dog', 'Boston Terrier', 1, 'Male', 'Healthy', 'Friendly and alert', 'Marley.png', '2024-02-02 00:00:00', 'Available', 7),
(37, 'Milo', 'Cat', 'American Shorthair', 2, 'Male', 'Healthy', 'Playful and curious', 'Milo.png', '2024-02-03 00:00:00', 'Available', 7),
(38, 'Penny', 'Dog', 'Shiba Inu', 4, 'Female', 'Healthy', 'Independent and spirited', 'Penny.png', '2024-02-04 00:00:00', 'Available', 7),
(39, 'Ruby', 'Cat', 'Scottish Fold', 1, 'Female', 'Healthy', 'Gentle and loving', 'Ruby.png', '2024-02-05 00:00:00', 'Available', 8),
(40, 'Thor', 'Dog', 'Akita', 5, 'Male', 'Healthy', 'Strong and dignified', 'Thor.png', '2024-02-06 00:00:00', 'Available', 8),
(41, 'Ella', 'Dog', 'Samoyed', 3, 'Female', 'Healthy', 'Friendly and fluffy', 'Ella.png', '2024-02-07 00:00:00', 'Available', 8),
(42, 'Oreo', 'Cat', 'Tuxedo', 2, 'Male', 'Healthy', 'Playful and active', 'Oreo.png', '2024-02-08 00:00:00', 'Available', 8),
(43, 'Daisy', 'Dog', 'Australian Shepherd', 1, 'Female', 'Healthy', 'Highly energetic', 'Daisy.png', '2024-02-09 00:00:00', 'Available', 8),
(44, 'Rosie', 'Cat', 'Ragamuffin', 4, 'Female', 'Healthy', 'Laid-back and affectionate', 'Rosie.png', '2024-02-10 00:00:00', 'Available', 9),
(45, 'Diesel', 'Dog', 'Pit Bull', 2, 'Male', 'Healthy', 'Loving and strong', 'Diesel.png', '2024-02-11 00:00:00', 'Available', 9),
(46, 'Simba', 'Cat', 'Exotic Shorthair', 1, 'Male', 'Healthy', 'Sweet and curious', 'Simba.png', '2024-02-12 00:00:00', 'Available', 9),
(47, 'Maggie', 'Dog', 'Cavalier King Charles Spaniel', 3, 'Female', 'Healthy', 'Friendly and gentle', 'Maggie.png', '2024-02-13 00:00:00', 'Available', 9),
(48, 'Archie', 'Dog', 'Weimaraner', 4, 'Male', 'Healthy', 'Energetic and loyal', 'Archie.png', '2024-02-14 00:00:00', 'Available', 9),
(49, 'Luna', 'Cat', 'Siberian', 2, 'Female', 'Healthy', 'Playful and affectionate', 'Luna.png', '2024-02-15 00:00:00', 'Available', 10),
(50, 'Rocky', 'Dog', 'Alaskan Malamute', 5, 'Male', 'Healthy', 'Strong and friendly', 'Rocky.png', '2024-02-16 00:00:00', 'Available', 10),
(51, 'Mochi', 'Cat', 'Turkish Van', 1, 'Female', 'Healthy', 'Energetic and unique', 'Mochi.png', '2024-02-17 00:00:00', 'Available', 10),
(52, 'Bruno', 'Dog', 'Newfoundland', 6, 'Male', 'Healthy', 'Gentle and giant', 'Bruno.png', '2024-02-18 00:00:00', 'Available', 10),
(53, 'Pixie', 'Cat', 'Pixie-Bob', 3, 'Female', 'Healthy', 'Adventurous and curious', 'Pixie.png', '2024-02-19 00:00:00', 'Available', 10),
(54, 'Lily', 'Cat', 'Birman', 2, 'Female', 'Healthy', 'Gentle and affectionate', 'Lily.png', '2024-01-26 00:00:00', 'Available', 6),
(55, 'Zeus', 'Dog', 'Rottweiler', 4, 'Male', 'Healthy', 'Strong and loyal', 'Zeus.png', '2024-01-27 00:00:00', 'Available', 6),
(56, 'Sunny', 'Bird', 'Parrot', 3, 'Female', 'Healthy', 'Colorful and talkative', 'Sunny.png', '2024-01-28 00:00:00', 'Available', 6),
(57, 'Finn', 'Dog', 'Cocker Spaniel', 2, 'Male', 'Healthy', 'Cheerful and friendly', 'Finn.png', '2024-01-29 00:00:00', 'Available', 6),
(58, 'Hopper', 'Rabbit', 'Lionhead', 1, 'Male', 'Healthy', 'Playful and fluffy', 'Hopper.png', '2024-01-30 00:00:00', 'Available', 6),
(59, 'Duke', 'Dog', 'Doberman', 5, 'Male', 'Healthy', 'Protective and intelligent', 'Duke.png', '2024-01-31 00:00:00', 'Available', 7),
(60, 'Coco', 'Cat', 'Himalayan', 3, 'Female', 'Healthy', 'Sweet and calm', 'Coco.png', '2024-02-01 00:00:00', 'Available', 7),
(61, 'Scales', 'Reptile', 'Bearded Dragon', 4, 'Male', 'Healthy', 'Calm and friendly', 'Scales.png', '2024-02-02 00:00:00', 'Available', 7),
(62, 'Milo', 'Cat', 'American Shorthair', 2, 'Male', 'Healthy', 'Playful and curious', 'Milo.png', '2024-02-03 00:00:00', 'Available', 7),
(63, 'Snowball', 'Rabbit', 'Netherland Dwarf', 1, 'Female', 'Healthy', 'Small and adorable', 'Snowball.png', '2024-02-04 00:00:00', 'Available', 7),
(64, 'Ruby', 'Cat', 'Scottish Fold', 1, 'Female', 'Healthy', 'Gentle and loving', 'Ruby.png', '2024-02-05 00:00:00', 'Available', 8),
(65, 'Thor', 'Dog', 'Akita', 5, 'Male', 'Healthy', 'Strong and dignified', 'Thor.png', '2024-02-06 00:00:00', 'Available', 8),
(66, 'Skye', 'Bird', 'Cockatiel', 2, 'Female', 'Healthy', 'Loves to sing', 'Skye.png', '2024-02-07 00:00:00', 'Available', 8),
(67, 'Oreo', 'Cat', 'Tuxedo', 2, 'Male', 'Healthy', 'Playful and active', 'Oreo.png', '2024-02-08 00:00:00', 'Available', 8),
(68, 'Daisy', 'Dog', 'Australian Shepherd', 1, 'Female', 'Healthy', 'Highly energetic', 'Daisy.png', '2024-02-09 00:00:00', 'Available', 8),
(69, 'Rosie', 'Cat', 'Ragamuffin', 4, 'Female', 'Healthy', 'Laid-back and affectionate', 'Rosie.png', '2024-02-10 00:00:00', 'Available', 9),
(70, 'Diesel', 'Dog', 'Pit Bull', 2, 'Male', 'Healthy', 'Loving and strong', 'Diesel.png', '2024-02-11 00:00:00', 'Available', 9),
(71, 'Nibbles', 'Rodent', 'Guinea Pig', 1, 'Male', 'Healthy', 'Cute and social', 'Nibbles.png', '2024-02-12 00:00:00', 'Available', 9),
(72, 'Maggie', 'Dog', 'Cavalier King Charles Spaniel', 3, 'Female', 'Healthy', 'Friendly and gentle', 'Maggie.png', '2024-02-13 00:00:00', 'Available', 9),
(73, 'Spike', 'Reptile', 'Leopard Gecko', 2, 'Male', 'Healthy', 'Calm and unique', 'Spike.png', '2024-02-14 00:00:00', 'Available', 9),
(74, 'Luna', 'Cat', 'Siberian', 2, 'Female', 'Healthy', 'Playful and affectionate', 'Luna.png', '2024-02-15 00:00:00', 'Available', 10),
(75, 'Rocky', 'Dog', 'Alaskan Malamute', 5, 'Male', 'Healthy', 'Strong and friendly', 'Rocky.png', '2024-02-16 00:00:00', 'Available', 10),
(76, 'Mochi', 'Cat', 'Turkish Van', 1, 'Female', 'Healthy', 'Energetic and unique', 'Mochi.png', '2024-02-17 00:00:00', 'Available', 10),
(77, 'Puff', 'Bird', 'Canary', 3, 'Male', 'Healthy', 'Melodious and vibrant', 'Puff.png', '2024-02-18 00:00:00', 'Available', 10),
(78, 'Squeaky', 'Rodent', 'Hamster', 1, 'Female', 'Healthy', 'Tiny and playful', 'Squeaky.png', '2024-02-19 00:00:00', 'Available', 10);

-- --------------------------------------------------------

--
-- Table structure for table `VB_Shelters`
--

CREATE TABLE `VB_Shelters` (
  `shelter_id` int NOT NULL,
  `shelter_name` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `contact` varchar(50) NOT NULL,
  `website_url` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `VB_Shelters`
--

INSERT INTO `VB_Shelters` (`shelter_id`, `shelter_name`, `address`, `contact`, `website_url`) VALUES
(1, 'Happy soul shelter', '456 Elm St, Springfield', '437128792', 'http://newwebsite.org'),
(2, 'Potsdam Shelter', 'Potsdam', '31243212', 'http://deqwf@fea.com'),
(3, 'Happy Paws Shelter', '123 Main St, Springfield', '555-123-4567', 'https://happypawshelter.org'),
(4, 'Canton Shelter', 'Canton', '4731481593', 'https://cantonshelter.com'),
(5, 'Happy Tails Shelter', '123 Main St, New York, NY', '123-456-7890', 'http://happytails.com'),
(6, 'Paws & Claws Rescue', '456 Oak Ave, Los Angeles, CA', '987-654-3210', 'http://pawsclawsrescue.com'),
(7, 'FurEver Home', '789 Maple Dr, Chicago, IL', '555-678-1234', 'http://fureverhome.org'),
(8, 'Safe Haven Shelter', '321 Pine Ln, Houston, TX', '333-222-1111', 'http://safehaven.com'),
(9, 'Whisker Wonderland', '654 Elm St, Miami, FL', '444-555-6666', 'http://whiskerwonderland.org'),
(10, 'Companion Rescue', '987 Cedar Rd, Seattle, WA', '777-888-9999', 'http://companionrescue.com'),
(11, 'Loving Paws Shelter', '159 Birch Blvd, Denver, CO', '222-333-4444', 'http://lovingpaws.org'),
(12, 'Tail Waggers Haven', '753 Willow Way, Phoenix, AZ', '888-777-6666', 'http://tailwaggers.com'),
(13, 'Purr & Bark Place', '246 Aspen Ave, Boston, MA', '111-222-3333', 'http://purrbarkplace.com'),
(14, 'Forever Friends Shelter', '135 Spruce St, San Francisco, CA', '666-555-4444', 'http://foreverfriends.com');

-- --------------------------------------------------------

--
-- Table structure for table `VB_Users`
--

CREATE TABLE `VB_Users` (
  `user_id` int NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `phone_number` varchar(50) NOT NULL,
  `registration_date` datetime NOT NULL,
  `Address` varchar(50) NOT NULL,
  `zipcode` int NOT NULL,
  `name` varchar(50) NOT NULL,
  `user_type` varchar(50) NOT NULL,
  `shelter_id` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `VB_Users`
--

INSERT INTO `VB_Users` (`user_id`, `email`, `password`, `phone_number`, `registration_date`, `Address`, `zipcode`, `name`, `user_type`, `shelter_id`) VALUES
(4, 'pawarv@example.com', '09fddf96d18c92c2fd795fd5cbc7dc33', '1234567890', '2024-11-18 00:00:00', '123 Main St', 12345, 'Pawar V', 'admin', 1),
(5, 'bhanu@example.com', 'adf47922f0bdb6b9a520ed2d43622d14', '1234567832', '2024-11-18 00:00:00', '123 Main St', 13676, 'Bhanu P', 'customer', 2),
(7, 'john@example.com', 'adf47922f0bdb6b9a520ed2d43622d14', '1234143', '2024-11-19 00:00:00', 'Canton', 13660, 'John Cena', 'customer', 1),
(8, 'Mike@example.com', 'adf47922f0bdb6b9a520ed2d43622d14', '1234135', '2024-11-18 00:00:00', 'Watertown', 13700, 'Mike Tyson', 'customer', 2),
(9, 'Tyler@example.com', 'a4eb2e0f3e0cbac5c3e64ddc4d24f1df', '133114531', '2024-11-20 00:00:00', 'Potsdam', 13699, 'Tyler', 'customer', NULL),
(10, 'Kshitij@example.com', 'adf47922f0bdb6b9a520ed2d43622d14', '831242134', '2024-12-01 00:00:00', 'Pierrepont Street', 13676, 'Kshitij', 'customer', NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `VB_Adoptions`
--
ALTER TABLE `VB_Adoptions`
  ADD PRIMARY KEY (`adoption_id`),
  ADD KEY `user_id` (`user_id`),
  ADD KEY `pet_id` (`pet_id`);

--
-- Indexes for table `VB_Appointments`
--
ALTER TABLE `VB_Appointments`
  ADD PRIMARY KEY (`appointment_id`),
  ADD KEY `shelter_id` (`shelter_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `VB_Pets`
--
ALTER TABLE `VB_Pets`
  ADD PRIMARY KEY (`pet_id`),
  ADD KEY `shelter_id` (`shelter_id`);

--
-- Indexes for table `VB_Shelters`
--
ALTER TABLE `VB_Shelters`
  ADD PRIMARY KEY (`shelter_id`);

--
-- Indexes for table `VB_Users`
--
ALTER TABLE `VB_Users`
  ADD PRIMARY KEY (`user_id`),
  ADD KEY `shelter_id` (`shelter_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `VB_Adoptions`
--
ALTER TABLE `VB_Adoptions`
  MODIFY `adoption_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `VB_Appointments`
--
ALTER TABLE `VB_Appointments`
  MODIFY `appointment_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `VB_Pets`
--
ALTER TABLE `VB_Pets`
  MODIFY `pet_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=79;

--
-- AUTO_INCREMENT for table `VB_Shelters`
--
ALTER TABLE `VB_Shelters`
  MODIFY `shelter_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `VB_Users`
--
ALTER TABLE `VB_Users`
  MODIFY `user_id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `VB_Adoptions`
--
ALTER TABLE `VB_Adoptions`
  ADD CONSTRAINT `VB_Adoptions_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `VB_Users` (`user_id`),
  ADD CONSTRAINT `VB_Adoptions_ibfk_2` FOREIGN KEY (`pet_id`) REFERENCES `VB_Pets` (`pet_id`);

--
-- Constraints for table `VB_Appointments`
--
ALTER TABLE `VB_Appointments`
  ADD CONSTRAINT `VB_Appointments_ibfk_1` FOREIGN KEY (`shelter_id`) REFERENCES `VB_Shelters` (`shelter_id`),
  ADD CONSTRAINT `VB_Appointments_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `VB_Users` (`user_id`);

--
-- Constraints for table `VB_Pets`
--
ALTER TABLE `VB_Pets`
  ADD CONSTRAINT `VB_Pets_ibfk_1` FOREIGN KEY (`shelter_id`) REFERENCES `VB_Shelters` (`shelter_id`);

--
-- Constraints for table `VB_Users`
--
ALTER TABLE `VB_Users`
  ADD CONSTRAINT `VB_Users_ibfk_1` FOREIGN KEY (`shelter_id`) REFERENCES `VB_Shelters` (`shelter_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
