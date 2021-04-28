#!/bin/sh
curl "https://"${1} -si | grep -w 'location:' | cut -c11-
