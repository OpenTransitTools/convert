- pip install poetry
- git clone https://github.com/OpenTransitTools/convert.git
- cd convert
- poetry install

CSV to JSON:
  - bin/csv_to_json data/gtfs_feeds.csv

OTP-UI localizations:
  - cd data
  - ./get_otpui_i18n.sh
  - cd ..
  - poetry run json2locs
  - ls *.json
