import React from 'react';
import PropTypes from 'prop-types';
import { Contacto } from '../../models/contacto.class';


const ComponenteB = ({ contacto }) => {
    return (
        <div>
            <h2>
                Nombre del Contacto: { contacto.nombre }
            </h2>
            <h3>
                Estado: { contacto.conectado ? 'Contacto en Línea':'Contacto No Disponible'}
            </h3>
        </div>
    );
};


ComponenteB.propTypes = {
    contacto: PropTypes.instanceOf(Contacto)
};


export default ComponenteB;
