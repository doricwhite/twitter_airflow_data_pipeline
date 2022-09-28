## Twitter Data Pipeline Using Apache Airflow

---

[Video Link](https://www.youtube.com/watch?v=q8q3OFFfY6c)

---

Possible Challenges You May Face:

- When trying to access the Twitter API, If you get the error "**_error 453 - You currently have Essential access which includes access to Twitter API v2 endpoints only_**", it could mean you only have "Essential" access to the API.

  - You would need to request "Elevated Access" from the Twitter API developer dashboard

- If you note the error **_Permissions 0644 for 'key_pair_name.pem' are too open_** when connecting to the EC2 instance, change the file permisson with the command below:

  - `chmod 400 key_pair_name.pem`

* I had some challenges with Airflow launching successfully when using the "Free tier eligible" (t2.micro) instance type when creating the EC2 instance.
  - This was resolve by using a t2.medium or higher instance type.

Any other challenge was addressed in the video.
