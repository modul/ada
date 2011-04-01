/* 
 * ADA - Analog data aquisition
 * 
 * Simple voltage reading with ATtiny25.
 *
 * author:  Remo Giermann <mo@liberejo.de>
 * created: 2011/03/19
 *
 */

#include <avr/io.h>
#include <avr/interrupt.h>
#include "softuart.h"

uint16_t read_adc(uint8_t adc);
void put_word(uint16_t word);

int main()
{
    char c;
    uint16_t adc = 0;

    softuart_init();
    sei();

    // enable ADC, VCC ref., set prescaler to 8
    ADCSRA = _BV(ADEN) | _BV(ADPS1) | _BV(ADPS0);

    while (1) {
        if (softuart_kbhit()) {
            c = softuart_getchar();
//            softuart_putchar(c);
           if (c == '1') {
               adc = read_adc(1);
               put_word(adc);
           }
           else if (c == '2') {
               adc = read_adc(2);
               put_word(adc);
           }
           else if (c == '3') {
               adc = read_adc(3);
               put_word(adc);
           } 
        }
    }

    return 0;
}

uint16_t read_adc(uint8_t adc)
{
    uint16_t a = 0;
    uint8_t  i = 0;

    ADMUX = adc;
            
    for (i=0; i < 4; i++) {          // read ADC, take 4 samples
        ADCSRA |= _BV(ADSC);         // start conversion
        while (ADCSRA & _BV(ADSC));  // wait till end of conversion
        a += ADCW;
    }
   
    a = a >> 2; // divide by 4 to get mean
                   
    return a;
}

void put_word(uint16_t word) 
{
    softuart_putchar((uint8_t) (word >> 8));
    softuart_putchar((uint8_t) (word & 0xFF));
}
