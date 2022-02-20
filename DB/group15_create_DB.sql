create table categories
(
    category_ID   int         not null
        primary key,
    category_name varchar(50) not null,
    img_url       text        not null
);

create table customers
(
    Email      varchar(255)                       not null
        primary key,
    Password   varchar(50)                        not null,
    First_name varchar(50)                        not null,
    Last_name  varchar(50)                        not null,
    Join_DT    datetime default CURRENT_TIMESTAMP not null
);

create table workshops
(
    workshop_ID   int auto_increment
        primary key,
    workshop_dt   datetime      not null,
    workshop_name varchar(50)   not null,
    img_url       text          not null,
    description1  varchar(2000) not null,
    description2  varchar(2000) null,
    price         int           not null,
    num_of_people int           not null
);

create table products
(
    product_ID   int          not null
        primary key,
    category_ID  int          not null,
    product_name varchar(50)  not null,
    price        int          not null,
    description  varchar(255) null,
    img_url      text         not null,
    constraint FK_category
        foreign key (category_ID) references categories (category_ID)
);

create table orders
(
    email             varchar(255)                       not null,
    order_creation_dt datetime default CURRENT_TIMESTAMP not null,
    arrival_dt        date                               not null,
    phone_number      int                                not null,
    address           varchar(50)                        not null,
    card              varchar(18)                        not null,
    ExpiryDate        date                               not null,
    cvv               varchar(3)                         not null,
    comment           varchar(200)                       null,
    totalPrice        int                                not null,
    primary key (email, order_creation_dt),
    constraint FK_customers
        foreign key (email) references customers (Email)
);

create table products_in_order
(
    email             varchar(255)                       not null,
    order_creation_dt datetime default CURRENT_TIMESTAMP not null,
    product_id        int                                not null,
    quantity          int                                not null,
    TotalPrice        int                                not null,
    primary key (email, order_creation_dt, product_id),
    constraint FK_Products
        foreign key (product_id) references products (product_ID),
    constraint FK_orders
        foreign key (email, order_creation_dt) references orders (email, order_creation_dt)
);

create table shopping_carts
(
    email      varchar(255) not null,
    product_ID int          not null,
    Quantity   int          not null,
    primary key (email, product_ID),
    constraint FK_email
        foreign key (email) references customers (Email),
    constraint FK_product
        foreign key (product_ID) references products (product_ID)
);

create table registrations_workshops
(
    email      varchar(255) not null,
    ws_ID      int          not null,
    ws_DT      datetime     not null,
    card       varchar(18)  not null,
    ExpiryDate date         not null,
    cvv        varchar(3)   not null,
    primary key (email, ws_ID, ws_DT),
    constraint FK_customer_id
        foreign key (email) references customers (Email),
    constraint FK_workshop
        foreign key (ws_ID) references workshops (workshop_ID)
);


