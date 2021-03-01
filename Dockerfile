# Build Vue
FROM node:14.5.0-alpine as build-stage
WORKDIR /app
COPY ./frontend/package*.json ./
RUN npm install
COPY ./frontend/ .
RUN npm run build

# Setup Container and install Flask
FROM lsiobase/alpine:3.12 as deploy-stage
# MAINTANER Your Name "info@selfhosted.pro"

# Set Variables
ENV FLASK_CONFIG=production
ENV PYTHONIOENCODING=UTF-8

WORKDIR /api
COPY ./backend ./

# Install Dependancies
RUN \
	# echo '**** adding repositories ****' && \
	# echo 'http://dl-cdn.alpinelinux.org/alpine/v3.6/main' >> /etc/apk/repositories && \
	# echo 'http://dl-cdn.alpinelinux.org/alpine/v3.6/community' >> /etc/apk/repositories && \
	# apk update && \
	echo "**** install build packages ****" && \
	apk add --no-cache --virtual=build-dependencies \
	g++ \
	make \
	python3-dev \
	libffi-dev \
	ruby-dev \
	curl && \
	echo "**** install packages ****" && \
	apk add --no-cache \
	python3 \
	py3-pip \
	# mongodb \
	nginx && \
	gem install sass &&\
	echo "**** Installing Python Modules ****" && \
	curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3 - && \
	$HOME/.poetry/bin/poetry export -f requirements.txt --output requirements.txt && \
	pip3 install wheel && \
	pip3 install -r requirements.txt && \
	echo "**** Cleaning Up ****" &&\
	apk del --purge \
	build-dependencies && \
	rm -rf \
	/root/.cache \
	/tmp/*

COPY root /

# Vue
COPY --from=build-stage /app/dist /app
COPY nginx.conf /etc/nginx/

# Expose
VOLUME /config
EXPOSE 8000