import sqlite3

# Connect to the database
conn = sqlite3.connect("reviews.db")
cur = conn.cursor()

# Data to insert (ignoring id as it's auto-increment)
data = [
    ('Vinay Sai Kishore', 'vinay2020@gmail.com', '7654321098', 'Hello', 5),
    ('Ananya Sharma', 'ananya.s@outlook.com', '9876543210', 'Great service!', 5),
    ('Rohan Mehra', 'rohanm88@yahoo.com', '8123456789', 'The app is a bit slow.', 3),
    ('Priya Das', 'priya.das@gmail.com', '7012345678', 'Excellent support team.', 5),
    ('Arjun Varma', 'arjunv@icloud.com', '9123456701', 'Needs more features.', 4),
    ('Sanya Malhotra', 'sanya.m@gmail.com', '8234567890', 'Loved the user interface!', 5),
    ('Vikram Singh', 'vicky.singh@protonmail.com', '9345678901', 'Buggy on Android.', 2),
    ('Ishita Paul', 'ishitap@gmail.com', '7456789012', 'Very intuitive to use.', 4),
    ('Karan Joshi', 'karanj@rediffmail.com', '8567890123', 'Average experience.', 3),
    ('Megha Nair', 'megha.n@gmail.com', '9678901234', 'Highly recommended!', 5),
    ('Aditya Rao', 'adiraonew@gmail.com', '7789012345', 'Pricing is too high.', 2),
    ('Sneha Gupta', 'sneha_g@outlook.com', '8890123456', 'Happy with the update.', 4),
    ('Rahul Bose', 'rbose_dev@gmail.com', '9901234567', 'Not working on Chrome.', 1),
    ('Tanvi Shah', 'tanvishah@gmail.com', '7011223344', 'Beautiful design.', 5),
    ('Abhishek Jha', 'abhi_jha@yahoo.co.in', '8122334455', 'Good, but could be better.', 3),
    ('Riya Sen', 'riya.sen@gmail.com', '9233445566', 'Fantastic experience.', 5),
    ('Manish Goel', 'mgoel87@gmail.com', '7344556677', 'Customer care was rude.', 1),
    ('Kavita Iyer', 'kavita.iyer@gmail.com', '8455667788', 'Easy navigation.', 4),
    ('Suresh Kumar', 'sureshk@hotmail.com', '9566778899', 'Value for money.', 5),
    ('Deepika Pal', 'deepu_pal@gmail.com', '7677889900', 'Confusing settings.', 2),
    ('Amitabh Roy', 'aroy_99@gmail.com', '8788990011', 'The best in the market.', 5),
    ('Neha Kapoor', 'neha.k@gmail.com', '9899001122', 'Loading takes too long.', 2),
    ('Varun Dhawan', 'v_dhawan@gmail.com', '7900112233', 'Superb!', 5),
    ('Pooja Hegde', 'pooja.h@yahoo.com', '8011223344', 'Satisfied with the result.', 4),
    ('Zaid Khan', 'zkhan88@gmail.com', '9122334455', "Can't login today.", 1),
    ('Simran Kaur', 'simran_k@gmail.com', '7233445566', 'Well done team.', 5),
    ('Farhan Ali', 'ali.farhan@gmail.com', '8344556677', 'Will use it again.', 4),
    ('Divya Bharti', 'divya.b@outlook.com', '9455667788', 'Decent performance.', 3),
    ('Kartik Aryan', 'kartik.a@gmail.com', '7566778899', 'Love the dark mode!', 5),
    ('Kiara Advani', 'kiara_adv@gmail.com', '8677889900', 'Helpful documentation.', 4),
    ('Siddharth M', 'sid_m@gmail.com', '9788990011', 'Too many ads.', 2),
    ('Rashmika M', 'rashu.m@gmail.com', '7899001122', 'Smooth animations.', 5),
    ('Vijay Sethu', 'v.sethu@yahoo.com', '8900112233', 'Functional and clean.', 4),
    ('Nayanthara K', 'nayan.k@gmail.com', '9011223344', 'Exceeded expectations.', 5),
    ('Prabhas Raju', 'prabhas_r@gmail.com', '7122334455', 'Great for beginners.', 4),
    ('Allu Arjun', 'allu.a@gmail.com', '8233445566', 'Stylish UI.', 5),
    ('Trisha Krish', 'trish.k@gmail.com', '9344556677', 'A bit overpriced.', 3),
    ('Yash Gowda', 'yash.rocky@gmail.com', '7455667788', 'Solid build quality.', 5),
    ('Samantha Ruth', 'sam_ruth@gmail.com', '8566778899', 'Quick response time.', 4),
    ('Dulquer S', 'dq_salman@gmail.com', '9677889900', 'Simply amazing.', 5),
    ('Naveen Polis', 'naveen.p@gmail.com', '7788990011', 'Crash on startup.', 1),
    ('Keerthy S', 'keerthy.s@gmail.com', '8899001122', 'Everything works well.', 4),
    ('Ram Charan', 'ram_charan@gmail.com', '9900112233', 'Top notch quality.', 5),
    ('Shruti Haasan', 'shruti.h@gmail.com', '7012345679', 'Better than competitors.', 5),
    ('Mahesh Babu', 'mahesh.b@gmail.com', '8123456780', 'Professional look.', 4),
    ('Kajal Aggarwal', 'kajal.a@gmail.com', '9234567891', 'Missing some filters.', 3),
    ('Rana Daggubati', 'rana_d@gmail.com', '7345678902', 'Great community.', 5),
    ('Tamannaah B', 'tammy.b@gmail.com', '8456789013', 'Satisfied customer.', 4),
    ('Nani Babu', 'nani.v@gmail.com', '9567890124', 'Impressive speed.', 5),
    ('Sai Pallavi', 'sai.pallavi@gmail.com', '7678901235', 'Pure excellence.', 5)
]

# Insert each row
for row in data:
    cur.execute(
        "INSERT INTO reviews (name, email, phone, review, rating) VALUES (?, ?, ?, ?, ?)",
        row
    )

# Commit and close
conn.commit()
conn.close()

print("Data inserted successfully!")
