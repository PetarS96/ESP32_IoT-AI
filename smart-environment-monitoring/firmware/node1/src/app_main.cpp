#include <stdio.h>
#include "driver/gpio.h"
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "esp_ipc.h"


// Pin definitions
#define BUTTON1_PIN GPIO_NUM_36  // GPIO36 (input)
#define BUTTON2_PIN GPIO_NUM_39  // GPIO39 (input)
#define LED1_PIN GPIO_NUM_32     // GPIO32 (output)
#define LED2_PIN GPIO_NUM_33     // GPIO33 (output)
#define LED3_PIN GPIO_NUM_25     // GPIO25 (output)

void configure_gpio(gpio_num_t pin, gpio_mode_t mode, gpio_pull_mode_t pull_mode);

void app_main(void) {
    // Initialize Serial for debugging
    printf("ESP32 GPIO Test\n");

    // Configure GPIO pins using the custom function
    configure_gpio(BUTTON1_PIN, GPIO_MODE_INPUT, GPIO_PULLDOWN_ONLY);  // Button 1 with pull-down
    configure_gpio(BUTTON2_PIN, GPIO_MODE_INPUT, GPIO_PULLDOWN_ONLY);  // Button 2 with pull-down
    configure_gpio(LED1_PIN, GPIO_MODE_OUTPUT, GPIO_FLOATING);         // LED 1 (no pull-up/pull-down)
    configure_gpio(LED2_PIN, GPIO_MODE_OUTPUT, GPIO_FLOATING);         // LED 2 (no pull-up/pull-down)
    configure_gpio(LED3_PIN, GPIO_MODE_OUTPUT, GPIO_FLOATING);         // LED 3 (no pull-up/pull-down)

    // Turn off all LEDs initially
    gpio_set_level(LED1_PIN, 0);
    gpio_set_level(LED2_PIN, 0);
    gpio_set_level(LED3_PIN, 0);

    while (1) {
        // Read button states
        bool button1State = gpio_get_level(BUTTON1_PIN);
        bool button2State = gpio_get_level(BUTTON2_PIN);

        // Control LEDs based on button states
        gpio_set_level(LED1_PIN, button1State);  // Turn on/off LED1
        gpio_set_level(LED2_PIN, button2State);  // Turn on/off LED2

        // Toggle LED3 every 500ms
        gpio_set_level(LED3_PIN, !gpio_get_level(LED3_PIN));
        vTaskDelay(500 / portTICK_PERIOD_MS); // 500ms delay
    }
}

// Custom GPIO configuration function
void configure_gpio(gpio_num_t pin, gpio_mode_t mode, gpio_pull_mode_t pull_mode) {
    gpio_config_t io_conf;
    io_conf.pin_bit_mask = (1ULL << pin);
    io_conf.mode = mode;
    io_conf.intr_type = GPIO_INTR_DISABLE;

    switch (pull_mode) {
        case GPIO_PULLUP_ONLY:
            io_conf.pull_down_en = GPIO_PULLDOWN_DISABLE;
            io_conf.pull_up_en = GPIO_PULLUP_ENABLE;
            break;
        case GPIO_PULLDOWN_ONLY:
            io_conf.pull_down_en = GPIO_PULLDOWN_ENABLE;
            io_conf.pull_up_en = GPIO_PULLUP_DISABLE;
            break;
        case GPIO_PULLUP_PULLDOWN:
            io_conf.pull_down_en = GPIO_PULLDOWN_ENABLE;
            io_conf.pull_up_en = GPIO_PULLUP_ENABLE;
            break;
        default:
            io_conf.pull_down_en = GPIO_PULLDOWN_DISABLE;
            io_conf.pull_up_en = GPIO_PULLUP_DISABLE;
            break;
    }

    gpio_config(&io_conf);
}
