# 🌐 Web Development Blog

This repository contains my work for the **Web Development course**.
The blog serves as a collection of assignments, projects, and learning exercises completed throughout the semester.

Each assignment is structured as a self-contained webpage, but they all live in this repo (and are linked together in the blog’s navigation).

Deployed on **GitHub Pages** for easy access.

👉 [Visit the Blog](https://piriyajeishree410.github.io/)

---

## Purpose of this Blog

* To document my journey in learning **HTML, CSS, JavaScript, and web development fundamentals**.
* To showcase completed assignments and mini-projects in a **live, interactive format**.
* To practice using **GitHub Pages for deployment**, **Git for version control**, and **Markdown for documentation**.

---

## 📚 Assignments

### Assignment 1: Getting Started with the Blog

* Set up this repository on GitHub.
* Configured **GitHub Pages** to serve the blog.
* Created a homepage with an introduction and navigation.
* Learned how to link external CSS and JavaScript files.

*This assignment laid the foundation for the blog, where all other assignments will be added.*

---

### Assignment 2: Airbnb Listings Demo Page

This assignment was about working with **AJAX, JSON, and dynamic content rendering with JavaScript**.
I repurposed the [Airbnb Listings Demo Project](https://github.com/john-guerra/Airbnb_Listings_demo_page) and customized it to meet all assignment requirements.

#### Features

* **Loads first 50 listings dynamically from JSON** (using `fetch` + `async/await`).
* **Each card displays:**

  * Listing name
  * Thumbnail image (with fallback placeholder)
  * Host name and photo (with fallback placeholder)
  * Price per night
  * Short description
  * Amenities (first 3 + “+N more”)
* **Creative additions:**

  * Search listings by name, description, or host.
  * Sort listings by price or rating.
  * Ratings displayed as stars.
* **Fallbacks:** Placeholder images and error handling for missing data.

#### Technical Details

* **JSON file:** `data/airbnb_listings.json` (50 listings generated via Python script).
* **JavaScript:** Fetches JSON, renders DOM elements, and updates UI on search/sort.
* **CSS:** Responsive grid layout, styled cards with hover effects.

#### Assignment Requirements Fulfilled

* Display first 50 listings from JSON via AJAX.
* Show name, description, amenities, host info, price, and thumbnail.
* Add one creative/interactive feature (search + sort + stars).
* Document with README + deployed on GitHub Pages.

#### Live Demo

👉 [Airbnb Listings Page](https://piriyajeishree410.github.io/)

---

## Project Structure

```
.
├── index.html               # Blog homepage (contains assignment 1+2 HTML and JS script along with the styles)
│   └── data/
│       └── airbnb_listings.json
└── README.md                 # Documentation (this file)
```

---

## Technologies Used

* HTML5
* CSS3
* JavaScript (ES6+, `fetch`, DOM manipulation, async/await)
* JSON
* Git & GitHub Pages

---

## Future work

I will try to create separate pages for each assignment so that everything is not listed on the homepage.

## Credits

* Inspired by [john-guerra/Airbnb\_Listings\_demo\_page](https://github.com/john-guerra/Airbnb_Listings_demo_page).
* Placeholder images: [Picsum](https://picsum.photos/) and [Pravatar](https://pravatar.cc/).
* JSON dataset generated using Python.

---

✨ Built as part of the **CSWeb Development course blog**.
