PGDMP     5    -                y           db_lab1    10.18    10.18 ,               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                       false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                       false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                       false                       1262    16510    db_lab1    DATABASE     ?   CREATE DATABASE db_lab1 WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'Ukrainian_Ukraine.1251' LC_CTYPE = 'Ukrainian_Ukraine.1251';
    DROP DATABASE db_lab1;
             postgres    false                        2615    2200    public    SCHEMA        CREATE SCHEMA public;
    DROP SCHEMA public;
             postgres    false                       0    0    SCHEMA public    COMMENT     6   COMMENT ON SCHEMA public IS 'standard public schema';
                  postgres    false    3                        3079    12924    plpgsql 	   EXTENSION     ?   CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;
    DROP EXTENSION plpgsql;
                  false                        0    0    EXTENSION plpgsql    COMMENT     @   COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';
                       false    1            ?            1259    16541    comments    TABLE     ?   CREATE TABLE public.comments (
    comment_id integer NOT NULL,
    comment_content character varying(100) NOT NULL,
    post_id integer NOT NULL,
    author_id integer NOT NULL,
    publication_date date NOT NULL
);
    DROP TABLE public.comments;
       public         postgres    false    3            ?            1259    16539    comments_comment_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.comments_comment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.comments_comment_id_seq;
       public       postgres    false    3    201            !           0    0    comments_comment_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.comments_comment_id_seq OWNED BY public.comments.comment_id;
            public       postgres    false    200            ?            1259    16528    posts    TABLE     ?   CREATE TABLE public.posts (
    post_id integer NOT NULL,
    post_content character varying(100) NOT NULL,
    author_id integer NOT NULL,
    publication_date date NOT NULL
);
    DROP TABLE public.posts;
       public         postgres    false    3            ?            1259    16526    posts_post_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.posts_post_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.posts_post_id_seq;
       public       postgres    false    199    3            "           0    0    posts_post_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.posts_post_id_seq OWNED BY public.posts.post_id;
            public       postgres    false    198            ?            1259    16583 
   posts_tags    TABLE     ^   CREATE TABLE public.posts_tags (
    post_id integer NOT NULL,
    tag_id integer NOT NULL
);
    DROP TABLE public.posts_tags;
       public         postgres    false    3            ?            1259    16559    tags    TABLE     g   CREATE TABLE public.tags (
    tag_id integer NOT NULL,
    tag_name character varying(50) NOT NULL
);
    DROP TABLE public.tags;
       public         postgres    false    3            ?            1259    16557    tags_tag_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.tags_tag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.tags_tag_id_seq;
       public       postgres    false    203    3            #           0    0    tags_tag_id_seq    SEQUENCE OWNED BY     C   ALTER SEQUENCE public.tags_tag_id_seq OWNED BY public.tags.tag_id;
            public       postgres    false    202            ?            1259    16518    users    TABLE     ?   CREATE TABLE public.users (
    user_id integer NOT NULL,
    login character varying(30) NOT NULL,
    fullname character varying(50) NOT NULL,
    registration_date date NOT NULL
);
    DROP TABLE public.users;
       public         postgres    false    3            ?            1259    16516    users_user_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.users_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.users_user_id_seq;
       public       postgres    false    197    3            $           0    0    users_user_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.users_user_id_seq OWNED BY public.users.user_id;
            public       postgres    false    196            ?
           2604    16544    comments comment_id    DEFAULT     z   ALTER TABLE ONLY public.comments ALTER COLUMN comment_id SET DEFAULT nextval('public.comments_comment_id_seq'::regclass);
 B   ALTER TABLE public.comments ALTER COLUMN comment_id DROP DEFAULT;
       public       postgres    false    201    200    201            ?
           2604    16531    posts post_id    DEFAULT     n   ALTER TABLE ONLY public.posts ALTER COLUMN post_id SET DEFAULT nextval('public.posts_post_id_seq'::regclass);
 <   ALTER TABLE public.posts ALTER COLUMN post_id DROP DEFAULT;
       public       postgres    false    198    199    199            ?
           2604    16562    tags tag_id    DEFAULT     j   ALTER TABLE ONLY public.tags ALTER COLUMN tag_id SET DEFAULT nextval('public.tags_tag_id_seq'::regclass);
 :   ALTER TABLE public.tags ALTER COLUMN tag_id DROP DEFAULT;
       public       postgres    false    203    202    203            ?
           2604    16521    users user_id    DEFAULT     n   ALTER TABLE ONLY public.users ALTER COLUMN user_id SET DEFAULT nextval('public.users_user_id_seq'::regclass);
 <   ALTER TABLE public.users ALTER COLUMN user_id DROP DEFAULT;
       public       postgres    false    196    197    197                      0    16541    comments 
   TABLE DATA               e   COPY public.comments (comment_id, comment_content, post_id, author_id, publication_date) FROM stdin;
    public       postgres    false    201   ?.                 0    16528    posts 
   TABLE DATA               S   COPY public.posts (post_id, post_content, author_id, publication_date) FROM stdin;
    public       postgres    false    199   /                 0    16583 
   posts_tags 
   TABLE DATA               5   COPY public.posts_tags (post_id, tag_id) FROM stdin;
    public       postgres    false    204   ?/                 0    16559    tags 
   TABLE DATA               0   COPY public.tags (tag_id, tag_name) FROM stdin;
    public       postgres    false    203   ?/                 0    16518    users 
   TABLE DATA               L   COPY public.users (user_id, login, fullname, registration_date) FROM stdin;
    public       postgres    false    197   0       %           0    0    comments_comment_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.comments_comment_id_seq', 3, true);
            public       postgres    false    200            &           0    0    posts_post_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.posts_post_id_seq', 5, true);
            public       postgres    false    198            '           0    0    tags_tag_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.tags_tag_id_seq', 3, true);
            public       postgres    false    202            (           0    0    users_user_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.users_user_id_seq', 5, true);
            public       postgres    false    196            ?
           2606    16546    comments comments_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_pkey PRIMARY KEY (comment_id);
 @   ALTER TABLE ONLY public.comments DROP CONSTRAINT comments_pkey;
       public         postgres    false    201            ?
           2606    16533    posts posts_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_pkey PRIMARY KEY (post_id);
 :   ALTER TABLE ONLY public.posts DROP CONSTRAINT posts_pkey;
       public         postgres    false    199            ?
           2606    16587    posts_tags posts_tags_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.posts_tags
    ADD CONSTRAINT posts_tags_pkey PRIMARY KEY (post_id, tag_id);
 D   ALTER TABLE ONLY public.posts_tags DROP CONSTRAINT posts_tags_pkey;
       public         postgres    false    204    204            ?
           2606    16564    tags tags_pkey 
   CONSTRAINT     P   ALTER TABLE ONLY public.tags
    ADD CONSTRAINT tags_pkey PRIMARY KEY (tag_id);
 8   ALTER TABLE ONLY public.tags DROP CONSTRAINT tags_pkey;
       public         postgres    false    203            ?
           2606    16523    users users_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);
 :   ALTER TABLE ONLY public.users DROP CONSTRAINT users_pkey;
       public         postgres    false    197            ?
           2606    16552     comments comments_author_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_author_id_fkey FOREIGN KEY (author_id) REFERENCES public.users(user_id);
 J   ALTER TABLE ONLY public.comments DROP CONSTRAINT comments_author_id_fkey;
       public       postgres    false    197    2697    201            ?
           2606    16547    comments comments_post_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.comments
    ADD CONSTRAINT comments_post_id_fkey FOREIGN KEY (post_id) REFERENCES public.posts(post_id);
 H   ALTER TABLE ONLY public.comments DROP CONSTRAINT comments_post_id_fkey;
       public       postgres    false    2699    199    201            ?
           2606    16534    posts posts_author_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.posts
    ADD CONSTRAINT posts_author_id_fkey FOREIGN KEY (author_id) REFERENCES public.users(user_id);
 D   ALTER TABLE ONLY public.posts DROP CONSTRAINT posts_author_id_fkey;
       public       postgres    false    199    2697    197            ?
           2606    16588 "   posts_tags posts_tags_post_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.posts_tags
    ADD CONSTRAINT posts_tags_post_id_fkey FOREIGN KEY (post_id) REFERENCES public.posts(post_id);
 L   ALTER TABLE ONLY public.posts_tags DROP CONSTRAINT posts_tags_post_id_fkey;
       public       postgres    false    204    2699    199            ?
           2606    16593 !   posts_tags posts_tags_tag_id_fkey    FK CONSTRAINT     ?   ALTER TABLE ONLY public.posts_tags
    ADD CONSTRAINT posts_tags_tag_id_fkey FOREIGN KEY (tag_id) REFERENCES public.tags(tag_id);
 K   ALTER TABLE ONLY public.posts_tags DROP CONSTRAINT posts_tags_tag_id_fkey;
       public       postgres    false    203    204    2703               k   x?3?t?O,)VT?H?T??/KU(?HU(.)MK??4?4?420??50?52?2??H,Q?,V??
?t?qUT0?3?4?4*32+3?2??,- 
C-u?b???? 8?Q         ?   x?E??
?0??볧8=??M?ٝW
5ÛnDJ??M·/#?????k?ڌ#?K?j???? ?\??~??:??UU;??HByB"???TT?=6}?1?rp??????4`?3"?	???Ce??}jU?5????s V??n??T?4-?e?W2??l?q?YLn[B?ث00            x?3?4?2?4?2b ;F??? ??         '   x?3??M,??2?,???,?L.?2?,.?/*?????? ???         ?   x?-?A
?0????)r?H&m@???n?+dP!?MFR
mOoټ??~??e8?S??`?5?HS???v???K????T??䰂??﯇S>u??????!?????I?nH??.????]?km?w??u=-*     