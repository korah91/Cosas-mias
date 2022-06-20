import React from 'react';
import PropTypes from 'prop-types';
import { Contacto } from '../../models/contacto.class';
import ComponenteB from '../pure/componenteB';

const ComponenteA = () => {

    const defaultComponenteB = new Contacto("Nombre", 'Apellido', 'Email', false);

    const changeState = (id) => {
        console.log('Cambiar estado de Contacto')
    }
    return (
        <div>
            <div>
                Your Contacts
            </div>
            <div>
                <ComponenteB contacto={defaultComponenteB}></ComponenteB>
            </div>
        </div>
    );
};


ComponenteA.propTypes = {

};


export default ComponenteA;
