# Use the official mariadb:10.5 image as a base
FROM mariadb:10.5

# Set environment variables
ENV MYSQL_DATABASE=portal_db \
    MYSQL_USER=sec_admin \
    MYSQL_PASSWORD=qwer1234!@ \
    MYSQL_ROOT_PASSWORD=qwer1234!@

# Copy custom configuration file (my.cnf) to container
#COPY my.cnf /etc/mysql/conf.d/

# Expose the port 3306
EXPOSE 3306
