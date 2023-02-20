import os
import stripe

from .models import Discount, Tax

stripe.api_key = os.getenv('SK_TOKEN')


def stripe_check_or_create_discount():
    new_discounts = Discount.objects.filter(stripe_id=None)
    if new_discounts.count():
        print('Есть новые скидки')
        for create_discount in new_discounts:
            print('id записи: ', create_discount.pk)
            edit_obj = Discount.objects.get(pk=create_discount.pk)
            print(edit_obj.amount)
            result = stripe.Coupon.create(
                percent_off=edit_obj.amount,
            )
            edit_obj.stripe_id = result.id
            edit_obj.save()
    else:
        print('Новых скидок нет')


def stripe_check_or_create_tax():
    new_taxes = Tax.objects.filter(txr=None)
    if new_taxes.count():
        print('Есть новые налоги в базе')
        for create_tax in new_taxes:
            print('id записи: ', create_tax.pk)
            edit_obj = Tax.objects.get(pk=create_tax.pk)
            result = stripe.TaxRate.create(
                display_name=create_tax.name,
                description=create_tax.description,
                inclusive=False,
                percentage=create_tax.amount
            )
            edit_obj.txr = result.id
            edit_obj.save()
    else:
        print('Новых налогов в базе нет')


def stripe_session_create_helper(name, price, tax, discount):
    line = [
        {
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': name,
                },
                'unit_amount': price * 100,
            },
            'quantity': 1,
            'tax_rates': []
        }
    ]
    discount_coupone = []
    if tax:
        line[0]['tax_rates'] = [tax]
    if discount:
        discount_coupone.append({'coupon': discount})
    session = stripe.checkout.Session.create(
            line_items=line,
            mode='payment',
            discounts=discount_coupone,
            success_url='http://localhost:8000/success',
    )
    return session
