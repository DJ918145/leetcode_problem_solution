        with orderseries as
        (
        select
            customer_id,
            order_date,
            customer_pref_delivery_date,
           ( case when order_date=customer_pref_delivery_date then 'immediate_order' else 'scheduled' end ) as order_type,
           row_number() over (partition by customer_id order by order_date asc) as row_num
           from
           delivery
        )
        select 

        round(sum(case when order_type='immediate_order' and row_num=1 then 1 else 0 end)*1.00/sum(case when row_num=1 then 1 else 0 end)*100, 2) as immediate_percentage
        from orderseries
        


           
