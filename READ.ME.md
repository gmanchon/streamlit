
This repo is on prod at https://wagon-data-streamlit.herokuapp.com/

The hosting is free, the site may take up to 30 seconds to load initially
* EU version : https://wagon-data-streamlit-eu.herokuapp.com/
* US version : https://wagon-data-streamlit.herokuapp.com/

# usage

You may run this on your machine:

``` bash
streamlit run demo.py
```

# prod

If you wish to deploy to prod on heroku, do not forget to configure your email address

``` bash
heroku config:set HEROKU_EMAIL_ADDRESS=your-email-address@email-provider.com
heroku ps:scale web=1
```
