Here's your **To-Do List App** README with added emojis for a more engaging and visually appealing format:

---

# 📝 To-Do List App Visit Live Demo: https://flaskmongo.glitch.me/

This is a simple **To-Do List app** built using **Flask** (Python web framework) and **MongoDB** (NoSQL database). The app allows users to add, mark as complete, and delete tasks.

![image](https://github.com/user-attachments/assets/e9eaaf52-fa5f-4366-8def-f3c6d052fc1e)

![image](https://github.com/user-attachments/assets/a91338f7-745e-4231-9c39-07de27b947c6)


## 📂 What's in this project?

← `README.md`: This file, where you can tell people what your To-Do List app does and how you built it.

← `app.py`: The main Python file for your app. It contains routes for adding, completing, and deleting tasks, and connects to the MongoDB database.

← `index.html`: The main web page for your To-Do List app. It uses HTML to define the structure and content of the page. This page displays the tasks and allows users to interact with them (add, complete, delete).

← `style.css`: CSS file that applies styles to your To-Do List. The styles give the page a clean, user-friendly design. It also includes animations like striking through completed tasks.

← `script.js`: If you'd like to add some interactivity or extend the app’s functionality with JavaScript, you can do so in this file.

## 🛠️ How to Use

1. **Clone this project** to your local machine or remix it directly on Glitch.
2. **Install dependencies**: Run `pip install flask pymongo` to install Flask and MongoDB Python drivers.
3. **Setup MongoDB**: Ensure you have a MongoDB account and a database (you can use MongoDB Atlas if you prefer a cloud solution).
4. **Run the Flask app**: Start the Flask development server with the command `python app.py`.
5. **Add tasks**: On the main page, you can add new tasks and manage them.

## ✨ Features

- **➕ Add new tasks**: Enter a task and click "Add".
- **✅ Mark tasks as complete**: Click "Mark as Complete" to strike through tasks.
- **❌ Delete tasks**: Remove tasks permanently from the list.

## 🎨 Customizing the App

- **🔗 Change the MongoDB URI**: Update the connection string in `app.py` with your MongoDB credentials.
- **🖌️ Styling**: Customize the `style.css` to modify the appearance of the app. You can also adjust the layout using flexbox or grid.
- **💻 Interactivity**: You can add more JavaScript functionality in `script.js`, such as animations or dynamic updates without refreshing the page.

## 🚀 Ready to share your To-Do List app?

To share your app, you can add these meta tags to the `<head>` section of `index.html` to improve SEO and enable social media sharing:

```html
<link rel="canonical" href="https://your-app-url.com/" />
<meta name="description" content="A simple To-Do List app built with Flask and MongoDB. Add, complete, and delete tasks!" />
<meta name="robots" content="index,follow" />
<meta property="og:title" content="To-Do List App" />
<meta property="og:type" content="website" />
<meta property="og:url" content="https://your-app-url.com/" />
<meta property="og:description" content="A simple To-Do List app built with Flask and MongoDB. Add, complete, and delete tasks!" />
<meta property="og:image" content="https://your-image-url.com/image.png" />
<meta name="twitter:card" content="summary" />
```

## 🌐 To Get Your MongoDB Connection String:

If you want to get a connection string like `mongodb+srv://test:test@cluster0.sxci1.mongodb.net/?retryWrites=true&w=majority`, follow these steps:

### 🔑 Steps to Get Your MongoDB Connection String:

1. **💻 Create a MongoDB Cluster (if you don’t have one):**
   - Go to [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) and create a free account (if you haven't already).
   - After signing in, click **"Build a Cluster"** to create a cluster. Choose the free tier (M0) for a free database.
   - Choose the cloud provider and region, then click **"Create Cluster"**.

2. **🔐 Set Up a Database User:**
   - Go to the **Database Access** section in the left menu.
   - Click **"Add New Database User"**.
   - Create a username and password for your database access.
   - Choose the appropriate roles (e.g., `readWrite` on your database), and click **"Add User"**.

3. **🔗 Get the Connection String:**
   - In the **Clusters** section, click **Connect** on your cluster.
   - Select **"Connect your application"**.
   - You will be given a connection string like this:
     ```bash
     mongodb+srv://<username>:<password>@cluster0.sxci1.mongodb.net/<dbname>?retryWrites=true&w=majority
     ```
     - Replace `<username>` with the database username you created.
     - Replace `<password>` with the password you set for that user.
     - Replace `<dbname>` with the name of the database you want to connect to. If you haven't created one, you can just use the default database name, e.g., `test`.

4. **💻 Use the Connection String in Your Code:**
   - Now that you have the connection string, you can use it in your code.
   - For example, in Python using `pymongo`:
     ```python
     from pymongo import MongoClient
     client = MongoClient("mongodb+srv://<username>:<password>@cluster0.sxci1.mongodb.net/<dbname>?retryWrites=true&w=majority")
     db = client.get_database()
     ```

### 🌟 Example:
If your database user is `myUser`, the password is `myPassword`, and you want to connect to a database called `myDatabase`, the connection string will look like:

Steps to Allow Anyone to Connect:
Log into MongoDB Atlas:

Go to MongoDB Atlas and log in to your account.
Select Your Project:

Choose the project where your cluster is located.
Navigate to Network Access:

In the left sidebar, under the Security section, click Network Access.
Add a New IP Access List Entry:

Click on the Add IP Address button.
Allow Connections from All IPs:

In the IP Address field, enter 0.0.0.0/0 to allow access from any IP address.
Add a Comment (Optional):

In the Comment field, you can add a note like: Allow connections from all IPs.
Save the Changes:

Click Confirm to save the entry.
Example:
IP Address: 0.0.0.0/0
Comment: Allow connections from all IPs
Warning:
Security Risk: Allowing connections from any IP address (0.0.0.0/0) exposes your MongoDB database to potential unauthorized access. It's recommended to limit access only to trusted IP addresses or use additional security measures like VPN or SSL/TLS encryption, especially in production environments.
If you decide to use 0.0.0.0/0 for unrestricted access, you may want to use a strong username and password for your database and ensure that your MongoDB cluster is secured with proper authentication mechanisms.

```bash
mongodb+srv://myUser:myPassword@cluster0.sxci1.mongodb.net/myDatabase?retryWrites=true&w=majority
```

---

Thanks 😊
