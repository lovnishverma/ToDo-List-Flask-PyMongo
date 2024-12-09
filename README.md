# To-Do List App

This is a simple To-Do List app built using **Flask** (Python web framework) and **MongoDB** (NoSQL database). The app allows users to add, mark as complete, and delete tasks.

## What's in this project?

← `README.md`: This file, where you can tell people what your To-Do List app does and how you built it.

← `app.py`: The main Python file for your app. It contains routes for adding, completing, and deleting tasks, and connects to the MongoDB database.

← `index.html`: The main web page for your To-Do List app. It uses HTML to define the structure and content of the page. This page displays the tasks and allows users to interact with them (add, complete, delete).

← `style.css`: CSS file that applies styles to your To-Do List. The styles give the page a clean, user-friendly design. It also includes animations like striking through completed tasks.

← `script.js`: If you'd like to add some interactivity or extend the app’s functionality with JavaScript, you can do so in this file.

## How to Use

1. **Clone this project** to your local machine or remix it directly on Glitch.
2. **Install dependencies**: Run `pip install flask pymongo` to install Flask and MongoDB Python drivers.
3. **Setup MongoDB**: Ensure you have a MongoDB account and a database (you can use MongoDB Atlas if you prefer a cloud solution).
4. **Run the Flask app**: Start the Flask development server with the command `python app.py`.
5. **Add tasks**: On the main page, you can add new tasks and manage them.

## Features

- **Add new tasks**: Enter a task and click "Add".
- **Mark tasks as complete**: Click "Mark as Complete" to strike through tasks.
- **Delete tasks**: Remove tasks permanently from the list.

## Customizing the App

- **Change the MongoDB URI**: Update the connection string in `app.py` with your MongoDB credentials.
- **Styling**: Customize the `style.css` to modify the appearance of the app. You can also adjust the layout using flexbox or grid.
- **Interactivity**: You can add more JavaScript functionality in `script.js`, such as animations or dynamic updates without refreshing the page.

## Ready to share your To-Do List app?

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
