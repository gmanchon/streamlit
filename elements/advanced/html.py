
import streamlit as st

def title():
    return 'Injecting HTML 🧙‍♂️'

def run():

    st.write('If you really want to go crazy with the content, why not inject a custom HTML element?')

    if st.checkbox('Show teachers'):
        image_size = st.slider('Zoom', 50, 250, 119)

        # https://kitt.lewagon.com/camps/414/contracts
        # document.querySelectorAll('tr').forEach(elt => {
        #     const img = elt.getElementsByTagName('img');
        #     if (img.length > 0) {
        #         const name = elt.getElementsByTagName('td')[1].innerText;
        #         const src = img[0].src;
        #         console.log(`'${name}' : '${src}',`);
        #     }
        # });

        TEACHERS = {
            'Bruno Lajoie' : 'https://avatars1.githubusercontent.com/u/22095643?v=4',
            'Kevin Robert' : 'https://avatars1.githubusercontent.com/u/9978111?v=4',
            'Julien Pelegri' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1563814498/fku9zvwyhuqkcpwoixls.jpg',
            'Sébastien Saunier' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1558950804/lxpghuy9ljoa9mcwrrby.jpg',
            'Damien Milon' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1532100716/quohyte0kozuvxlwgn0s.jpg',
            'Benjamin Baranger' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1536827206/ixr9unj1pvqtkfbzvlcu.jpg',
            'Lucien George' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1581954281/yufygsunlebymjwtxqpi.jpg',
            'Zuza Żuber' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1570609465/a8kmugjdqlihecdk9cz8.jpg',
            'Benjamin Auzanneau' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1570874395/gykb7mofng5jiumfhxih.jpg',
            'Igor Koval' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1570875813/iwzfmio7d8n4qghlx00w.jpg',
            'Jean Bizot' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1570875224/ocypfncdlmcpxd1v60zp.jpg',
            'Hadrien Jean' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1570874079/b0jtipxjdruewdjiwjrh.jpg',
            'Davy Wai' : 'https://avatars3.githubusercontent.com/u/42499767?v=4',
            'Gaëtan Manchon' : 'https://avatars1.githubusercontent.com/u/34584935?v=4',
            'Matthieu Rousseau' : 'https://avatars0.githubusercontent.com/u/16851063?v=4',
            'Aurélien Allard' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1510128505/glgkbr1dc52wihgokplh.jpg',
            'Soumia Ghalim' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1587463683/xqicgayidgkjzkwd2gvn.jpg',
            'Paul Chabbert' : 'https://avatars2.githubusercontent.com/u/47640935?v=4',
            'Loïc Chesneau' : 'https://avatars3.githubusercontent.com/u/21106392?v=4',
            'Eloïse Gomez' : 'https://avatars2.githubusercontent.com/u/52004932?v=4',
            'Thibault Pedelhez' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1570454328/ma72namffbsh1vlso3c8.jpg',
            'Hugo Vandernotte' : 'https://res.cloudinary.com/wagon/image/upload/c_fill,g_face,h_200,w_200/v1516582640/xgp9icrtsu0bzt2jtjrl.jpg',
            'Victor Challier' : 'https://avatars2.githubusercontent.com/u/36234477?v=4',
            'Julien Parenti' : 'https://avatars1.githubusercontent.com/u/22306617?v=4'
        }

        TEACHER_CSS = f"""
        #teachers {{
            display: flex;
            flex-wrap: wrap;
        }}

        .teacher-card {{
            display: flex;
            flex-direction: column;
        }}

        .teacher-card img {{
            width: {image_size}px;
            height: {image_size}px;
            border-radius: 100%;
            padding: 4px;
            margin: 10px;
            box-shadow: 0 0 4px #eee;
        }}

        .teacher-card span {{
            text-align: center;
        }}
        """

        # streamlit html injection seems to sensitive to new lines...
        # remove that \ and the html gets displayed instead of being interpreted
        TEACHER_CARD = """\
            <div class="teacher-card">
                <img src="{url}">
                <span>{name}</span>
            </div>
        """

        teachers = ''.join([TEACHER_CARD.format(name=f'{name.split()[0]}', url=url) for name, url in TEACHERS.items()])

        TEACHER_HTML = f"""
        <style>
        {TEACHER_CSS}
        </style>
        <div id="teachers">
            {teachers}
        </div>
        """

        st.write(TEACHER_HTML, unsafe_allow_html=True)
