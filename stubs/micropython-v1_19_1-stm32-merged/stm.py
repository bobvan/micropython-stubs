"""
functionality specific to STM32 MCUs. See: https://docs.micropython.org/en/v1.19.1/library/stm.html

This module provides functionality specific to STM32 microcontrollers, including
direct access to peripheral registers.
"""
# MCU: {'ver': 'v1.19.1', 'build': '', 'platform': 'stm32', 'port': 'stm32', 'machine': 'PYBv1.1 with STM32F405RG', 'release': '1.19.1', 'nodename': 'pyboard', 'name': 'micropython', 'family': 'micropython', 'sysname': 'pyboard', 'version': '1.19.1'}
# Stubber: 1.9.11
from typing import Tuple, Any

SPI_I2SPR = 32  # type: int
RTC_DR = 4  # type: int
RTC_CR = 8  # type: int
RTC_CALR = 60  # type: int
RTC_ISR = 12  # type: int
RTC_SSR = 40  # type: int
RTC_SHIFTR = 44  # type: int
RTC_PRER = 16  # type: int
RTC_CALIBR = 24  # type: int
RTC_BKP5R = 100  # type: int
RTC_BKP4R = 96  # type: int
RTC_BKP3R = 92  # type: int
RTC_BKP6R = 104  # type: int
RTC_BKP9R = 116  # type: int
RTC_BKP8R = 112  # type: int
RTC_BKP7R = 108  # type: int
RTC_TAFCR = 64  # type: int
SPI_CR1 = 0  # type: int
SPI3 = 1073757184  # type: int
SPI2 = 1073756160  # type: int
SPI_CR2 = 4  # type: int
SPI_I2SCFGR = 28  # type: int
SPI_DR = 12  # type: int
SPI_CRCPR = 16  # type: int
SPI1 = 1073819648  # type: int
RTC_TSSSR = 56  # type: int
RTC_TSDR = 52  # type: int
RTC_TR = 0  # type: int
RTC_TSTR = 48  # type: int
SDIO = 1073818624  # type: int
RTC_WUTR = 20  # type: int
RTC_WPR = 36  # type: int
RTC_BKP2R = 88  # type: int
RNG = 1342572544  # type: int
RCC_SSCGR = 128  # type: int
RCC_PLLI2SCFGR = 132  # type: int
RNG_CR = 0  # type: int
RTC = 1073752064  # type: int
RNG_SR = 4  # type: int
RNG_DR = 8  # type: int
RCC_PLLCFGR = 4  # type: int
RCC_BDCR = 112  # type: int
RCC_APB2RSTR = 36  # type: int
RCC_APB2LPENR = 100  # type: int
RCC_CFGR = 8  # type: int
RCC_CSR = 116  # type: int
RCC_CR = 0  # type: int
RCC_CIR = 12  # type: int
RTC_ALRMAR = 28  # type: int
RTC_BKP16R = 144  # type: int
RTC_BKP15R = 140  # type: int
RTC_BKP14R = 136  # type: int
RTC_BKP17R = 148  # type: int
RTC_BKP1R = 84  # type: int
RTC_BKP19R = 156  # type: int
RTC_BKP18R = 152  # type: int
RTC_BKP13R = 132  # type: int
RTC_ALRMBSSR = 72  # type: int
RTC_ALRMBR = 32  # type: int
RTC_ALRMASSR = 68  # type: int
RTC_BKP0R = 80  # type: int
RTC_BKP12R = 128  # type: int
RTC_BKP11R = 124  # type: int
RTC_BKP10R = 120  # type: int
WWDG_SR = 8  # type: int
SPI_RXCRCR = 20  # type: int
TIM_RCR = 48  # type: int
TIM_PSC = 40  # type: int
TIM_OR = 80  # type: int
TIM_SMCR = 8  # type: int
UART5 = 1073762304  # type: int
UART4 = 1073761280  # type: int
TIM_SR = 16  # type: int
TIM_EGR = 20  # type: int
TIM_CR1 = 0  # type: int
TIM_CNT = 36  # type: int
TIM_CCR4 = 64  # type: int
TIM_CR2 = 4  # type: int
TIM_DMAR = 76  # type: int
TIM_DIER = 12  # type: int
TIM_DCR = 72  # type: int
USART1 = 1073811456  # type: int
USB_OTG_FS = 1342177280  # type: int
USART_SR = 0  # type: int
USART_GTPR = 24  # type: int
USB_OTG_HS = 1074003968  # type: int
WWDG_CR = 0  # type: int
WWDG_CFR = 4  # type: int
WWDG = 1073753088  # type: int
USART_DR = 4  # type: int
USART6 = 1073812480  # type: int
USART3 = 1073760256  # type: int
USART2 = 1073759232  # type: int
USART_BRR = 8  # type: int
USART_CR3 = 20  # type: int
USART_CR2 = 16  # type: int
USART_CR1 = 12  # type: int
TIM_CCR3 = 60  # type: int
TIM1 = 1073807360  # type: int
SYSCFG_PMC = 4  # type: int
SYSCFG_MEMRMP = 0  # type: int
TIM10 = 1073824768  # type: int
TIM13 = 1073748992  # type: int
TIM12 = 1073747968  # type: int
TIM11 = 1073825792  # type: int
SYSCFG_EXTICR3 = 20  # type: int
SYSCFG = 1073821696  # type: int
SPI_TXCRCR = 24  # type: int
SPI_SR = 8  # type: int
SYSCFG_CMPCR = 32  # type: int
SYSCFG_EXTICR2 = 16  # type: int
SYSCFG_EXTICR1 = 12  # type: int
SYSCFG_EXTICR0 = 8  # type: int
TIM14 = 1073750016  # type: int
TIM_CCER = 32  # type: int
TIM_BDTR = 68  # type: int
TIM_ARR = 44  # type: int
TIM_CCMR1 = 24  # type: int
TIM_CCR2 = 56  # type: int
TIM_CCR1 = 52  # type: int
TIM_CCMR2 = 28  # type: int
TIM9 = 1073823744  # type: int
TIM4 = 1073743872  # type: int
TIM3 = 1073742848  # type: int
TIM2 = 1073741824  # type: int
TIM5 = 1073744896  # type: int
TIM8 = 1073808384  # type: int
TIM7 = 1073746944  # type: int
TIM6 = 1073745920  # type: int
EXTI_SWIER = 16  # type: int
DAC_DOR1 = 44  # type: int
DAC_DHR8RD = 40  # type: int
DAC_DHR8R2 = 28  # type: int
DAC_DOR2 = 48  # type: int
DBGMCU = 3758366720  # type: int
DAC_SWTRIGR = 4  # type: int
DAC_SR = 52  # type: int
DAC_DHR8R1 = 16  # type: int
DAC_DHR12L2 = 24  # type: int
DAC_DHR12L1 = 12  # type: int
DAC_CR = 0  # type: int
DAC_DHR12LD = 36  # type: int
DAC_DHR12RD = 32  # type: int
DAC_DHR12R2 = 20  # type: int
DAC_DHR12R1 = 8  # type: int
DBGMCU_APB1FZ = 8  # type: int
EXTI_EMR = 4  # type: int
EXTI = 1073822720  # type: int
DMA_LISR = 0  # type: int
EXTI_FTSR = 12  # type: int
EXTI_RTSR = 8  # type: int
EXTI_PR = 20  # type: int
EXTI_IMR = 0  # type: int
DMA_LIFCR = 8  # type: int
DBGMCU_IDCODE = 0  # type: int
DBGMCU_CR = 4  # type: int
DBGMCU_APB2FZ = 12  # type: int
DMA1 = 1073897472  # type: int
DMA_HISR = 4  # type: int
DMA_HIFCR = 12  # type: int
DMA2 = 1073898496  # type: int
DAC1 = 1073771520  # type: int
ADC_JDR3 = 68  # type: int
ADC_JDR2 = 64  # type: int
ADC_JDR1 = 60  # type: int
ADC_JDR4 = 72  # type: int
ADC_JOFR3 = 28  # type: int
ADC_JOFR2 = 24  # type: int
ADC_JOFR1 = 20  # type: int
ADC_HTR = 36  # type: int
ADC2 = 1073815808  # type: int
ADC123_COMMON = 1073816320  # type: int
ADC1 = 1073815552  # type: int
ADC3 = 1073816064  # type: int
ADC_DR = 76  # type: int
ADC_CR2 = 8  # type: int
ADC_CR1 = 4  # type: int
ADC_JOFR4 = 32  # type: int
CRC = 1073885184  # type: int
CAN2 = 1073768448  # type: int
CAN1 = 1073767424  # type: int
CRC_CR = 8  # type: int
DAC = 1073771520  # type: int
CRC_IDR = 4  # type: int
CRC_DR = 0  # type: int
ADC_SR = 0  # type: int
ADC_SMPR1 = 12  # type: int
ADC_LTR = 40  # type: int
ADC_JSQR = 56  # type: int
ADC_SMPR2 = 16  # type: int
ADC_SQR3 = 52  # type: int
ADC_SQR2 = 48  # type: int
ADC_SQR1 = 44  # type: int
RCC_APB2ENR = 68  # type: int
FLASH = 1073888256  # type: int
IWDG = 1073754112  # type: int
I2S3EXT = 1073758208  # type: int
I2S2EXT = 1073755136  # type: int
IWDG_KR = 0  # type: int
IWDG_SR = 12  # type: int
IWDG_RLR = 8  # type: int
IWDG_PR = 4  # type: int
I2C_TRISE = 32  # type: int
I2C_DR = 16  # type: int
I2C_CR2 = 4  # type: int
I2C_CR1 = 0  # type: int
I2C_OAR1 = 8  # type: int
I2C_SR2 = 24  # type: int
I2C_SR1 = 20  # type: int
I2C_OAR2 = 12  # type: int
PWR = 1073770496  # type: int
RCC_AHB3LPENR = 88  # type: int
RCC_AHB3ENR = 56  # type: int
RCC_AHB2RSTR = 20  # type: int
RCC_AHB3RSTR = 24  # type: int
RCC_APB1RSTR = 32  # type: int
RCC_APB1LPENR = 96  # type: int
RCC_APB1ENR = 64  # type: int
RCC_AHB2LPENR = 84  # type: int
RCC = 1073887232  # type: int
PWR_CSR = 4  # type: int
PWR_CR = 0  # type: int
RCC_AHB1ENR = 48  # type: int
RCC_AHB2ENR = 52  # type: int
RCC_AHB1RSTR = 16  # type: int
RCC_AHB1LPENR = 80  # type: int
I2C_CCR = 28  # type: int
GPIOD = 1073875968  # type: int
GPIOC = 1073874944  # type: int
GPIOB = 1073873920  # type: int
GPIOE = 1073876992  # type: int
GPIOH = 1073880064  # type: int
GPIOG = 1073879040  # type: int
GPIOF = 1073878016  # type: int
GPIOA = 1073872896  # type: int
FLASH_KEYR = 4  # type: int
FLASH_CR = 16  # type: int
FLASH_ACR = 0  # type: int
FLASH_OPTCR = 20  # type: int
FLASH_SR = 12  # type: int
FLASH_OPTKEYR = 8  # type: int
FLASH_OPTCR1 = 24  # type: int
GPIOI = 1073881088  # type: int
GPIO_OTYPER = 4  # type: int
GPIO_OSPEEDR = 8  # type: int
GPIO_ODR = 20  # type: int
GPIO_PUPDR = 12  # type: int
I2C3 = 1073765376  # type: int
I2C2 = 1073764352  # type: int
I2C1 = 1073763328  # type: int
GPIO_MODER = 0  # type: int
GPIO_BSRR = 24  # type: int
GPIO_AFR1 = 36  # type: int
GPIO_AFR0 = 32  # type: int
GPIO_BSRRH = 26  # type: int
GPIO_LCKR = 28  # type: int
GPIO_IDR = 16  # type: int
GPIO_BSRRL = 24  # type: int
mem32: Any  ## <class 'mem'> = <32-bit memory>
mem8: Any  ## <class 'mem'> = <8-bit memory>
mem16: Any  ## <class 'mem'> = <16-bit memory>
