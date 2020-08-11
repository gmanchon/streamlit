
This repo is on prod at https://wagon-data-streamlit.herokuapp.com/

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
