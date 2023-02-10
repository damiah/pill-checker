# Build step #1: build the React front end
FROM node:lts-alpine as build-step
WORKDIR /app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json  ./
# COPY ./src ./src
# COPY ./public ./public
COPY . .
RUN npm install
EXPOSE 8080

# RUN npm run build
CMD [ "npm", "start" ]
# RUN npm start

# # Build step #2: build an Caddy container
# FROM caddy:alpine
# EXPOSE 80
# EXPOSE 443
# COPY --from=build-step /app/build /usr/share/caddy