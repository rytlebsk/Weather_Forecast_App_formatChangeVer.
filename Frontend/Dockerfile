FROM node:22-alpine

# Set the working directory inside the container to /app
WORKDIR /app

# Copy the package.json from Frontend to /app in the container
COPY ./package.json /package-lock.json ./

# Install dependencies
RUN npm install -g npm@latest

# Copy the entire source code from Frontend to /app/src
COPY . /app

# Expose port 8081
EXPOSE 8081

# Start the app
CMD ["npx", "expo","start"]
