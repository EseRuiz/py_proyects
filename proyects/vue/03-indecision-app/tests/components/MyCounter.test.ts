import { describe, test } from 'vitest';
import { mount } from '@vue/test-utils';
//import MyCounter from '../../../src/components/MyCounter.vue';
import MyCounter from '@/components/MyCounter.vue';

describe('<MyCounter>', () => {
  test('should match snapshot', () => {
    const wrapper = mount(MyCounter, {
      props: {
        value: 5
      }
    });

    expect(wrapper.html()).toMatchSnapshot();
  });

  test('verificar el valor del contador renderizado', () => {
    const value = 5;
    const wrapper = mount(MyCounter, {
      props: {
        value: value
      }
    });
    const [counterLabel, squareLabel] = wrapper.findAll('h3');

    expect(wrapper.find('h3').text()).toContain(`Counter: ${value}`);
    expect(wrapper.find('[data-testid="square-label"]').text()).toContain(
      `Square: ${value * value}`
    );
    // console.log(wrapper.find('h3').text());
    // console.log(wrapper.html());
    expect(counterLabel.text()).toContain(`Counter: ${value}`);
    expect(squareLabel.text()).toContain(`Square: ${value * value}`);
  });

  test('increments the counter when +1 button is clicked', async () => {
    const value = 6;
    const wrapper = mount(MyCounter, {
      props: {
        value: value
      }
    });

    const [counterLabel, squareLabel] = wrapper.findAll('h3');

    const btnIncrement = wrapper.find('button');
    await btnIncrement.trigger('click');

    expect(counterLabel.text()).toContain(`Counter: ${value}`);
    expect(squareLabel.text()).toContain(`Square: ${value * value}`);
  });

  test('decrements the counter when -1 button is clicked twice', async () => {
    const value = 5;
    const wrapper = mount(MyCounter, {
      props: {
        value: value
      }
    });

    const [counterLabel, squareLabel] = wrapper.findAll('h3');

    const [, btnDecrement] = wrapper.findAll('button');
    await btnDecrement.trigger('click');
    await btnDecrement.trigger('click');

    expect(counterLabel.text()).toContain(`Counter: ${value}`);
    expect(squareLabel.text()).toContain(`Square: ${value * value}`);
  });
});